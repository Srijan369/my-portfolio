from django.core.management.base import BaseCommand
from portfolio_app.models import SocialLink

class Command(BaseCommand):
    help = 'Add all social media links to the database'

    def handle(self, *args, **kwargs):
        self.stdout.write('Adding all social media links...')
        
        # Clear existing social links (optional - remove if you want to keep existing)
        SocialLink.objects.all().delete()
        
        # All social media links
        social_links = [
            {'platform': 'Facebook', 'url': '#', 'icon_class': 'bx bxl-facebook', 'order': 1},
            {'platform': 'Instagram', 'url': '#', 'icon_class': 'bx bxl-instagram', 'order': 2},
            {'platform': 'WhatsApp', 'url': '#', 'icon_class': 'bx bxl-whatsapp', 'order': 3},
            {'platform': 'LinkedIn', 'url': '#', 'icon_class': 'bx bxl-linkedin', 'order': 4},
            {'platform': 'GitHub', 'url': '#', 'icon_class': 'bx bxl-github', 'order': 5},
            {'platform': 'Twitter', 'url': '#', 'icon_class': 'bx bxl-twitter', 'order': 6},
            {'platform': 'YouTube', 'url': '#', 'icon_class': 'bx bxl-youtube', 'order': 7},
            {'platform': 'Discord', 'url': '#', 'icon_class': 'bx bxl-discord-alt', 'order': 8},
            {'platform': 'Telegram', 'url': '#', 'icon_class': 'bx bxl-telegram', 'order': 9},
            {'platform': 'X', 'url': '#', 'icon_class': 'bx bx-x', 'order': 10},
        ]
        
        for link in social_links:
            obj, created = SocialLink.objects.get_or_create(
                platform=link['platform'],
                defaults={
                    'url': link['url'],
                    'icon_class': link['icon_class'],
                    'order': link['order']
                }
            )
            if created:
                self.stdout.write(f'✓ Created social link: {link["platform"]}')
            else:
                self.stdout.write(f'⚠ Social link already exists: {link["platform"]}')
        
        self.stdout.write(self.style.SUCCESS(f'\n✅ Added {len(social_links)} social media links successfully!'))
        self.stdout.write('\n📝 To update URLs:')
        self.stdout.write('  1. Go to http://127.0.0.1:8000/admin')
        self.stdout.write('  2. Click on "Social links"')
        self.stdout.write('  3. Edit each link with your actual profile URLs')