from django.core.management.base import BaseCommand
from django.db import transaction
from apps.users.factories import UserFactory
from apps.users.models import User


class Command(BaseCommand):
    help = 'Users app uchun test ma\'lumotlarini yaratadi'

    def add_arguments(self, parser):
        parser.add_argument(
            '--users',
            type=int,
            default=20,
            help='Yaratilishi kerak bo\'lgan foydalanuvchilar soni (default: 20)',
        )
        parser.add_argument(
            '--with-admin',
            action='store_true',
            help='Admin foydalanuvchini yaratish',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Mavjud ma\'lumotlarni o\'chirish (superuser ni saqlab qoladi)',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data()
        
        self.create_data(
            users_count=options['users'],
            create_admin=options['with_admin']
        )

    def clear_data(self):
        """Mavjud ma'lumotlarni o'chirish"""
        self.stdout.write(
            self.style.WARNING('Users app ma\'lumotlari o\'chirilmoqda (superuser lar saqlanadi)...')
        )
        
        with transaction.atomic():
            # Oddiy foydalanuvchilarni o'chirish, superuser larni qoldirish
            User.objects.filter(is_superuser=False).delete()
        
        self.stdout.write(
            self.style.SUCCESS('Users app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, users_count, create_admin=False):
        """Ma'lumotlarni yaratish"""
        self.stdout.write(
            self.style.SUCCESS('Users app uchun ma\'lumotlar yaratilmoqda...')
        )
        
        created_users = 0
        
        # Admin yaratish
        if create_admin:
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
                    created_users += 1
                    self.stdout.write(f"Admin foydalanuvchi yaratildi: {admin_user.username}")
                else:
                    self.stdout.write(f"Admin foydalanuvchi allaqachon mavjud: {admin_user.username}")
            except Exception as e:
                self.stdout.write(f"Admin foydalanuvchi yaratishda xatolik: {e}")

        with transaction.atomic():
            # Oddiy foydalanuvchilarni yaratish
            self.stdout.write('Oddiy foydalanuvchilar yaratilmoqda...')
            users = []
            for i in range(users_count):
                user = UserFactory()
                users.append(user)
                created_users += 1
            self.stdout.write(f'{users_count} ta oddiy foydalanuvchi yaratildi')

            # Ba'zi foydalanuvchilarni staff qilish
            staff_count = max(1, users_count // 10)  # 10% ni staff qilish
            staff_users = users[:staff_count]
            for user in staff_users:
                user.is_staff = True
                user.save()
            self.stdout.write(f'{staff_count} ta staff foydalanuvchi yaratildi')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nUsers app uchun ma\'lumotlar muvaffaqiyatli yaratildi!\n'
                f'Jami foydalanuvchilar: {created_users}\n'
                f'Staff foydalanuvchilar: {staff_count if not create_admin else staff_count + 1}\n'
                f'Admin foydalanuvchilar: {1 if create_admin else 0}'
            )
        )
