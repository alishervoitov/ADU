from django.core.management.base import BaseCommand
from django.db import transaction
from apps.blog.factories import InteractiveServiceFactory
from apps.blog.models.services import InteractiveService
from apps.users.models import User


class Command(BaseCommand):
    help = 'Blog app uchun test ma\'lumotlarini yaratadi'

    def add_arguments(self, parser):
        parser.add_argument(
            '--services',
            type=int,
            default=20,
            help='Yaratilishi kerak bo\'lgan interaktiv xizmatlar soni (default: 20)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Mavjud ma\'lumotlarni o\'chirish',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data()
        
        self.create_data(services_count=options['services'])

    def clear_data(self):
        """Mavjud ma'lumotlarni o'chirish"""
        self.stdout.write(
            self.style.WARNING('Blog app ma\'lumotlari o\'chirilmoqda...')
        )
        
        with transaction.atomic():
            InteractiveService.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Blog app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, services_count):
        """Ma'lumotlarni yaratish"""
        self.stdout.write(
            self.style.SUCCESS('Blog app uchun ma\'lumotlar yaratilmoqda...')
        )
        
        # Admin user olish
        admin_user = None
        try:
            admin_user = User.objects.filter(is_superuser=True).first()
            if not admin_user:
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
            self.stdout.write(f"Admin foydalanuvchi topishda xatolik: {e}")

        with transaction.atomic():
            # Interaktiv xizmatlarni yaratish
            self.stdout.write('Interaktiv xizmatlar yaratilmoqda...')
            services = []
            for i in range(services_count):
                service = InteractiveServiceFactory(
                    created_by=admin_user,
                    updated_by=admin_user
                )
                services.append(service)
            self.stdout.write(f'{services_count} ta interaktiv xizmat yaratildi')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nBlog app uchun ma\'lumotlar muvaffaqiyatli yaratildi!\n'
                f'Interaktiv xizmatlar: {services_count}\n'
            )
        )
