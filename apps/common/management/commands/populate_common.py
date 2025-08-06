from django.core.management.base import BaseCommand
from django.db import transaction
from apps.common.factories import FrontendTranslationFactory
from apps.common.models import FrontendTranslation
from apps.users.models import User


class Command(BaseCommand):
    help = 'Common app uchun test ma\'lumotlarini yaratadi'

    def add_arguments(self, parser):
        parser.add_argument(
            '--translations',
            type=int,
            default=50,
            help='Yaratilishi kerak bo\'lgan tarjimalar soni (default: 50)',
        )
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Mavjud ma\'lumotlarni o\'chirish',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.clear_data()
        
        self.create_data(translations_count=options['translations'])

    def clear_data(self):
        """Mavjud ma'lumotlarni o'chirish"""
        self.stdout.write(
            self.style.WARNING('Common app ma\'lumotlari o\'chirilmoqda...')
        )
        
        with transaction.atomic():
            FrontendTranslation.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Common app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, translations_count):
        """Ma'lumotlarni yaratish"""
        self.stdout.write(
            self.style.SUCCESS('Common app uchun ma\'lumotlar yaratilmoqda...')
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
            # Tarjimalarni yaratish
            self.stdout.write('Frontend tarjimalari yaratilmoqda...')
            translations = []
            for i in range(translations_count):
                translation = FrontendTranslationFactory(
                    created_by=admin_user,
                    updated_by=admin_user
                )
                translations.append(translation)
            self.stdout.write(f'{translations_count} ta frontend tarjima yaratildi')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nCommon app uchun ma\'lumotlar muvaffaqiyatli yaratildi!\n'
                f'Frontend tarjimalari: {translations_count}\n'
            )
        )
