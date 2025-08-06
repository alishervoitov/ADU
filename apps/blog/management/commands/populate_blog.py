from django.core.management.base import BaseCommand
from django.db import transaction
from apps.blog.factories import InteractiveServiceFactory, FAQFactory
from apps.blog.models.services import InteractiveService
from apps.blog.models.faq import FAQ
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
            '--faqs',
            type=int,
            default=15,
            help='Yaratilishi kerak bo\'lgan FAQ lar soni (default: 15)',
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
            services_count=options['services'],
            faqs_count=options['faqs']
        )

    def clear_data(self):
        """Mavjud ma'lumotlarni o'chirish"""
        self.stdout.write(
            self.style.WARNING('Blog app ma\'lumotlari o\'chirilmoqda...')
        )
        
        with transaction.atomic():
            FAQ.objects.all().delete()
            InteractiveService.objects.all().delete()
        
        self.stdout.write(
            self.style.SUCCESS('Blog app ma\'lumotlari muvaffaqiyatli o\'chirildi!')
        )

    def create_data(self, services_count, faqs_count):
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
            # Agar ma'lumotlar mavjud bo'lsa, yaratmaslik
            existing_services = InteractiveService.objects.count()
            existing_faqs = FAQ.objects.count()

            if existing_services == 0:
                # Interaktiv xizmatlarni yaratish
                self.stdout.write('Interaktiv xizmatlar yaratilmoqda...')
                for i in range(services_count):
                    service = InteractiveServiceFactory(
                        created_by=admin_user,
                        updated_by=admin_user
                    )
                self.stdout.write(f'{services_count} ta interaktiv xizmat yaratildi')
            else:
                self.stdout.write(f'Interaktiv xizmatlar allaqachon mavjud ({existing_services} ta)')

            if existing_faqs == 0:
                # FAQ larni yaratish
                self.stdout.write('FAQ lar yaratilmoqda...')
                for i in range(faqs_count):
                    faq = FAQFactory(
                        created_by=admin_user,
                        updated_by=admin_user
                    )
                self.stdout.write(f'{faqs_count} ta FAQ yaratildi')
            else:
                self.stdout.write(f'FAQ lar allaqachon mavjud ({existing_faqs} ta)')

        self.stdout.write(
            self.style.SUCCESS(
                f'\nBlog app uchun ma\'lumotlar muvaffaqiyatli tekshirildi/yaratildi!\n'
                f'Interaktiv xizmatlar: {InteractiveService.objects.count()}\n'
                f'FAQ lar: {FAQ.objects.count()}\n'
            )
        )
