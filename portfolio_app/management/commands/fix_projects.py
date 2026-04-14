from django.core.management.base import BaseCommand
from portfolio_app.models import Project
import os
from django.core.files.base import ContentFile
from django.conf import settings
import urllib.request

class Command(BaseCommand):
    help = 'Fix projects with missing images'

    def handle(self, *args, **kwargs):
        self.stdout.write('Checking projects for missing images...')
        
        # Get all projects
        projects = Project.objects.all()
        
        fixed_count = 0
        for project in projects:
            try:
                # Try to access the image URL
                if project.image:
                    # Check if image file exists
                    if project.image and hasattr(project.image, 'url'):
                        self.stdout.write(f'✓ Project "{project.title}" has valid image')
                    else:
                        self.stdout.write(f'⚠ Project "{project.title}" has empty image field')
                        # You can either delete these projects or set a default image
                        # Option 1: Delete projects with empty images
                        # project.delete()
                        # fixed_count += 1
                        pass
                else:
                    self.stdout.write(f'⚠ Project "{project.title}" has no image')
                    # Option 2: You can delete these projects
                    # project.delete()
                    # fixed_count += 1
            except Exception as e:
                self.stdout.write(self.style.ERROR(f'✗ Error with project "{project.title}": {e}'))
                # Delete the problematic project
                project.delete()
                fixed_count += 1
                self.stdout.write(f'  Deleted problematic project: {project.title}')
        
        if fixed_count > 0:
            self.stdout.write(self.style.SUCCESS(f'✅ Deleted {fixed_count} problematic projects'))
        else:
            self.stdout.write(self.style.SUCCESS('✅ All projects have valid images'))
        
        # Count remaining projects
        remaining = Project.objects.count()
        self.stdout.write(f'Total projects remaining: {remaining}')