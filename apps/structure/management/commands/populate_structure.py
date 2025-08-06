from django.core.management.base import BaseCommand
from django.db import transaction
import random
from apps.structure.factories.factories import (
    EmployeeFactory, FacultyFactory, DepartmentFactory, 
    SpecialtyFactory, FacultyEmployeeFactory, DepartmentEmployeeFactory
)
from apps.structure.factories.main_info import HomePageTextFactory
from apps.structure.models.employees import Employee
from apps.structure.models.university import Faculty, Department, Specialty, FacultyEmployee, DepartmentEmployee
from apps.users.models import User
from apps.structure.models import HomePageText, UniversityBaseInfo


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
            '--home-page-texts',
            type=int,
            default=16,  # 4 ta type uchun har biridan 4 tadan
            help='Yaratilishi kerak bo\'lgan bosh sahifa matnlari soni (default: 16)',
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
            specialties_count=options['specialties'],
            home_page_texts_count=options['home_page_texts']
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
            HomePageText.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Structure app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, employees_count, faculties_count, departments_count, specialties_count, home_page_texts_count):
        """Ma'lumotlarni yaratish"""
        self.stdout.write(
            self.style.SUCCESS('Structure app uchun ma\'lumotlar yaratilmoqda...')
        )
        
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
            # Universitet Base ma'lumoti, agar mavjud bo'lmasa
            if not UniversityBaseInfo.objects.exists():
                UniversityBaseInfo.objects.create(
                    about="Andijon davlat universiteti haqida qisqacha ma'lumot.",
                    students_count=12000,
                    teachers_count=800,
                    faculty_count=12,
                    department_count=19,
                    phone_num="+998 74 123 45 67",
                    email="info@adu.uz",
                    address="Andijon sh., Universitet ko'chasi, 1-uy"
                )
            # Fakultetlarni yaratish
            self.stdout.write('Fakultetlar yaratilmoqda...')
            faculties = []
            existing_faculties_count = Faculty.objects.count()
            needed_faculties = max(0, faculties_count - existing_faculties_count)
            
            # Mavjud fakultetlarni olish
            faculties.extend(list(Faculty.objects.all()))
            
            # Yetishmagan fakultetlarni yaratish
            for i in range(needed_faculties):
                faculty = FacultyFactory()
                faculties.append(faculty)
            self.stdout.write(f'{needed_faculties} ta yangi fakultet yaratildi (jami: {len(faculties)})')

            # Xodimlarni yaratish
            self.stdout.write('Xodimlar yaratilmoqda...')
            employees = []
            existing_employees_count = Employee.objects.count()
            needed_employees = max(0, employees_count - existing_employees_count)
            
            # Mavjud xodimlarni olish
            employees.extend(list(Employee.objects.all()))
            
            # Yetishmagan xodimlarni yaratish
            for i in range(needed_employees):
                employee = EmployeeFactory()
                employees.append(employee)
            self.stdout.write(f'{needed_employees} ta yangi xodim yaratildi (jami: {len(employees)})')

            # Kafedralarni yaratish
            self.stdout.write('Kafedralar yaratilmoqda...')
            departments = []
            existing_departments_count = Department.objects.count()
            needed_departments = max(0, departments_count - existing_departments_count)
            
            # Mavjud kafedralarni olish
            departments.extend(list(Department.objects.all()))
            
            # Yetishmagan kafedralarni yaratish
            if needed_departments > 0 and faculties:
                for i in range(needed_departments):
                    # Random fakultetni tanlash
                    faculty = random.choice(faculties)
                    
                    department = DepartmentFactory(faculty=faculty)
                    departments.append(department)
            self.stdout.write(f'{needed_departments} ta yangi kafedra yaratildi (jami: {len(departments)})')

            # Yo'nalishlarni yaratish
            self.stdout.write('Yo\'nalishlar yaratilmoqda...')
            existing_specialties_count = Specialty.objects.count()
            needed_specialties = max(0, specialties_count - existing_specialties_count)
            
            specialties_created = 0
            if needed_specialties > 0 and departments:
                for i in range(needed_specialties):
                    # Random kafedradan boshlab, uning fakultetini olish
                    department = random.choice(departments)
                    faculty = department.faculty
                    
                    SpecialtyFactory(
                        faculty=faculty,
                        department=department
                    )
                    specialties_created += 1
            self.stdout.write(f'{specialties_created} ta yangi yo\'nalish yaratildi')

            # Fakultet xodimlarini yaratish
            self.stdout.write('Fakultet xodimlari tayinlanmoqda...')
            faculty_employees_count = 0
            for faculty in faculties[:5]:  # Faqat birinchi 5 ta fakultet uchun
                for _ in range(3):  # Har bir fakultetga 3 ta xodim
                    employee = random.choice(employees)
                    try:
                        FacultyEmployeeFactory(
                            faculty=faculty,
                            employee=employee
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
                            employee=employee
                        )
                        department_employees_count += 1
                    except:
                        # Duplicate bo'lishi mumkin, o'tkazib yuborish
                        pass
            self.stdout.write(f'{department_employees_count} ta kafedra xodimi tayinlandi')

            # Bosh sahifa matnlarini yaratish
            self.stdout.write('Bosh sahifa matnlari yaratilmoqda...')
            from apps.structure.models.main_info import MENU_PARTS
            
            home_page_texts_created = 0
            texts_per_type = home_page_texts_count // len(MENU_PARTS)  # Har bir type uchun nechta
            
            for menu_type, menu_name in MENU_PARTS:
                # Har bir type uchun mavjud matnlar sonini tekshirish
                existing_texts_for_type = HomePageText.objects.filter(type=menu_type).count()
                needed_texts_for_type = max(0, texts_per_type - existing_texts_for_type)
                
                for i in range(needed_texts_for_type):
                    try:
                        if menu_type == 'main':
                            # main type uchun URL bilan yaratish
                            HomePageTextFactory(
                                type=menu_type,
                                title=f"{menu_name} - {existing_texts_for_type + i + 1}",
                                url=f"https://adu.uz/{menu_type}/{existing_texts_for_type + i + 1}"
                            )
                        else:
                            # Boshqa typelar uchun URL siz
                            HomePageTextFactory(
                                type=menu_type,
                                title=f"{menu_name} - {existing_texts_for_type + i + 1}"
                            )
                        home_page_texts_created += 1
                    except Exception as e:
                        self.stdout.write(f"HomePageText yaratishda xatolik: {e}")
                        
            self.stdout.write(f'{home_page_texts_created} ta yangi bosh sahifa matni yaratildi')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nStructure app uchun ma\'lumotlar muvaffaqiyatli yaratildi!\n'
                f'Fakultetlar: {needed_faculties} yangi (jami: {len(faculties)})\n'
                f'Xodimlar: {needed_employees} yangi (jami: {len(employees)})\n'
                f'Kafedralar: {needed_departments} yangi (jami: {len(departments)})\n'
                f'Yo\'nalishlar: {specialties_created} yangi\n'
                f'Fakultet xodimlari: {faculty_employees_count}\n'
                f'Kafedra xodimlari: {department_employees_count}\n'
                f'Bosh sahifa matnlari: {home_page_texts_created} yangi'
            )
        )
