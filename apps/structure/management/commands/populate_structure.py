from django.core.management.base import BaseCommand
from django.db import transaction
import random
from apps.structure.factories import (
    EmployeeFactory, FacultyFactory, DepartmentFactory, 
    SpecialtyFactory, FacultyEmployeeFactory, DepartmentEmployeeFactory
)
from apps.structure.models.employees import Employee
from apps.structure.models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee
from apps.users.models import User


class Command(BaseCommand):
    help = 'Structure app uchun test ma\'lumotlarini yaratadi'

    def add_arguments(self, parser):
        parser.add_argument(
            '--employees',
            type=int,
            default=50,
            help='Yaratilishi kerak bo\'lgan xodimlar soni (default: 50)',
        )
        parser.add_argument(
            '--faculties',
            type=int,
            default=10,
            help='Yaratilishi kerak bo\'lgan fakultetlar soni (default: 10)',
        )
        parser.add_argument(
            '--departments',
            type=int,
            default=30,
            help='Yaratilishi kerak bo\'lgan kafedralar soni (default: 30)',
        )
        parser.add_argument(
            '--specialties',
            type=int,
            default=60,
            help='Yaratilishi kerak bo\'lgan yo\'nalishlar soni (default: 60)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Mavjud ma\'lumotlarni o\'chirish',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data()
        
        self.create_data(
            employees_count=options['employees'],
            faculties_count=options['faculties'],
            departments_count=options['departments'],
            specialties_count=options['specialties']
        )

    def clear_data(self):
        """Mavjud ma'lumotlarni o'chirish"""
        self.stdout.write(
            self.style.WARNING('Structure app ma\'lumotlari o\'chirilmoqda...')
        )
        
        with transaction.atomic():
            DepartmentEmployee.objects.all().delete()
            FacultyEmployee.objects.all().delete()
            Specialty.objects.all().delete()
            Department.objects.all().delete()
            Faculty.objects.all().delete()
            Employee.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Structure app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, employees_count, faculties_count, departments_count, specialties_count):
        """Ma'lumotlarni yaratish"""
        self.stdout.write(
            self.style.SUCCESS('Structure app uchun ma\'lumotlar yaratilmoqda...')
        )
        
        # Agar ma'lumotlar mavjud bo'lsa, qayta yaratmaslik
        existing_faculties = Faculty.objects.count()
        if existing_faculties > 0:
            self.stdout.write(f'Structure app da allaqachon ma\'lumotlar mavjud ({existing_faculties} ta fakultet)')
            self.stdout.write('Agar yangisini yaratmoqchi bo\'lsangiz, avval --clear ishlatib tozalang')
            return
        
        # Superuser yaratish (agar mavjud bo'lmasa)
        admin_user = None
        try:
            admin_user, created = User.objects.get_or_create(
                username='admin',
                defaults={
                    'email': 'admin@adu.uz',
                    'is_staff': True,
                    'is_superuser': True,
                    'first_name': 'Admin',
                    'last_name': 'User'
                }
            )
            if created:
                admin_user.set_password('admin123')
                admin_user.save()
                self.stdout.write(f"Admin foydalanuvchi yaratildi: {admin_user.username}")
        except Exception as e:
            self.stdout.write(f"Admin foydalanuvchi yaratishda xatolik: {e}")

        with transaction.atomic():
            # Fakultetlarni yaratish
            self.stdout.write('Fakultetlar yaratilmoqda...')
            faculties = []
            for i in range(faculties_count):
                faculty = FacultyFactory(
                    created_by=admin_user,
                    updated_by=admin_user
                )
                faculties.append(faculty)
            self.stdout.write(f'{faculties_count} ta fakultet yaratildi')

            # Xodimlarni yaratish
            self.stdout.write('Xodimlar yaratilmoqda...')
            employees = []
            for i in range(employees_count):
                employee = EmployeeFactory(
                    created_by=admin_user,
                    updated_by=admin_user
                )
                employees.append(employee)
            self.stdout.write(f'{employees_count} ta xodim yaratildi')

            # Kafedralarni yaratish
            self.stdout.write('Kafedralar yaratilmoqda...')
            departments = []
            for i in range(departments_count):
                # Random fakultetni tanlash
                faculty = random.choice(faculties)
                
                department = DepartmentFactory(
                    faculty=faculty,
                    created_by=admin_user,
                    updated_by=admin_user
                )
                departments.append(department)
            self.stdout.write(f'{departments_count} ta kafedra yaratildi')

            # Yo'nalishlarni yaratish
            self.stdout.write('Yo\'nalishlar yaratilmoqda...')
            for i in range(specialties_count):
                # Random kafedradan boshlab, uning fakultetini olish
                department = random.choice(departments)
                faculty = department.faculty
                
                SpecialtyFactory(
                    faculty=faculty,
                    department=department,
                    created_by=admin_user,
                    updated_by=admin_user
                )
            self.stdout.write(f'{specialties_count} ta yo\'nalish yaratildi')

            # Fakultet xodimlarini yaratish
            self.stdout.write('Fakultet xodimlari tayinlanmoqda...')
            faculty_employees_count = 0
            for faculty in faculties[:5]:  # Faqat birinchi 5 ta fakultet uchun
                for _ in range(3):  # Har bir fakultetga 3 ta xodim
                    employee = random.choice(employees)
                    try:
                        FacultyEmployeeFactory(
                            faculty=faculty,
                            employee=employee,
                            created_by=admin_user,
                            updated_by=admin_user
                        )
                        faculty_employees_count += 1
                    except:
                        # Duplicate bo'lishi mumkin, o'tkazib yuborish
                        pass
            self.stdout.write(f'{faculty_employees_count} ta fakultet xodimi tayinlandi')

            # Kafedra xodimlarini yaratish
            self.stdout.write('Kafedra xodimlari tayinlanmoqda...')
            department_employees_count = 0
            for department in departments[:10]:  # Faqat birinchi 10 ta kafedra uchun
                for _ in range(2):  # Har bir kafedraga 2 ta xodim
                    employee = random.choice(employees)
                    try:
                        DepartmentEmployeeFactory(
                            department=department,
                            employee=employee,
                            created_by=admin_user,
                            updated_by=admin_user
                        )
                        department_employees_count += 1
                    except:
                        # Duplicate bo'lishi mumkin, o'tkazib yuborish
                        pass
            self.stdout.write(f'{department_employees_count} ta kafedra xodimi tayinlandi')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nStructure app uchun ma\'lumotlar muvaffaqiyatli yaratildi!\n'
                f'Fakultetlar: {faculties_count}\n'
                f'Xodimlar: {employees_count}\n'
                f'Kafedralar: {departments_count}\n'
                f'Yo\'nalishlar: {specialties_count}\n'
                f'Fakultet xodimlari: {faculty_employees_count}\n'
                f'Kafedra xodimlari: {department_employees_count}'
            )
        )
