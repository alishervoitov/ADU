from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    help = 'Barcha applar uchun test ma\'lumotlarini yaratadi'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear-all',
            action='store_true',
            help='Barcha app lardagi mavjud ma\'lumotlarni o\'chirish',
        )
        parser.add_argument(
            '--users-only',
            action='store_true',
            help='Faqat users app uchun ma\'lumot yaratish',
        )
        parser.add_argument(
            '--structure-only',
            action='store_true',
            help='Faqat structure app uchun ma\'lumot yaratish',
        )
        parser.add_argument(
            '--blog-only',
            action='store_true',
            help='Faqat blog app uchun ma\'lumot yaratish',
        )
        parser.add_argument(
            '--common-only',
            action='store_true',
            help='Faqat common app uchun ma\'lumot yaratish',
        )

    def handle(self, *args, **options):
        self.stdout.write(
            self.style.SUCCESS('Barcha applar uchun ma\'lumotlar yaratilmoqda...\n')
        )

        # Faqat bitta app uchun
        if options['users_only']:
            self.populate_users(options['clear_all'])
            return
        
        if options['structure_only']:
            self.populate_structure(options['clear_all'])
            return
            
        if options['blog_only']:
            self.populate_blog(options['clear_all'])
            return
            
        if options['common_only']:
            self.populate_common(options['clear_all'])
            return

        # Barcha applar uchun
        self.populate_users(options['clear_all'])
        self.populate_structure(options['clear_all'])
        self.populate_blog(options['clear_all'])
        self.populate_common(options['clear_all'])
        
        self.stdout.write(
            self.style.SUCCESS('\n' + '='*50)
        )
        self.stdout.write(
            self.style.SUCCESS('Barcha applar uchun ma\'lumotlar muvaffaqiyatli yaratildi!')
        )
        self.stdout.write(
            self.style.SUCCESS('='*50)
        )

    def populate_users(self, clear_data=False):
        """Users app uchun ma'lumot yaratish"""
        self.stdout.write(self.style.HTTP_INFO('\n1. Users app...'))
        args = ['--users', '25', '--with-admin']
        if clear_data:
            args.append('--clear')
        call_command('populate_users', *args)

    def populate_structure(self, clear_data=False):
        """Structure app uchun ma'lumot yaratish"""
        self.stdout.write(self.style.HTTP_INFO('\n2. Structure app...'))
        args = ['--employees', '40', '--faculties', '8', '--departments', '25', '--specialties', '50']
        if clear_data:
            args.append('--clear')
        call_command('populate_structure', *args)

    def populate_blog(self, clear_data=False):
        """Blog app uchun ma'lumot yaratish"""
        self.stdout.write(self.style.HTTP_INFO('\n3. Blog app...'))
        args = ['--services', '15', '--faqs', '12']
        if clear_data:
            args.append('--clear')
        call_command('populate_blog', *args)
