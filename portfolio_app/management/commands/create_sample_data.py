from django.core.management.base import BaseCommand
from portfolio_app.models import Skill, Service, Project, Profile, SocialLink
from django.core.files.base import ContentFile
import os

class Command(BaseCommand):
    help = 'Create sample data for testing'

    def handle(self, *args, **kwargs):
        self.stdout.write('Creating sample data...')
        
        # Create Profile (only if none exists)
        if not Profile.objects.exists():
            profile = Profile.objects.create(
                name='Shiva',
                title='AI Developer',
                bio='I am an Artificial Intelligence Developer with a strong foundation in Python and Data Science. My work focuses on designing and implementing intelligent systems to solve complex problems.',
                email='shiva@example.com',
                phone='+91 9876543210',
                location='Varanasi, India'
            )
            self.stdout.write(self.style.SUCCESS('✓ Profile created'))
        
        # Create Social Links
        social_links = [
            {'platform': 'GitHub', 'url': 'https://github.com/shiva', 'icon_class': 'bx bxl-github', 'order': 1},
            {'platform': 'LinkedIn', 'url': 'https://linkedin.com/in/shiva', 'icon_class': 'bx bxl-linkedin', 'order': 2},
            {'platform': 'Twitter', 'url': 'https://twitter.com/shiva', 'icon_class': 'bx bxl-twitter', 'order': 3},
            {'platform': 'Instagram', 'url': 'https://instagram.com/shiva', 'icon_class': 'bx bxl-instagram', 'order': 4},
        ]
        
        for link in social_links:
            obj, created = SocialLink.objects.get_or_create(
                platform=link['platform'],
                defaults=link
            )
            if created:
                self.stdout.write(f'✓ Created social link: {link["platform"]}')
        
        # Create Technical Skills
        tech_skills = [
            {'name': 'HTML', 'category': 'technical', 'percentage': 85, 'icon_class': 'bx bxl-html5', 'color': '#E34C26', 'order': 1},
            {'name': 'CSS', 'category': 'technical', 'percentage': 80, 'icon_class': 'bx bxl-css3', 'color': '#264de4', 'order': 2},
            {'name': 'JavaScript', 'category': 'technical', 'percentage': 75, 'icon_class': 'bx bxl-javascript', 'color': '#F7DF1E', 'order': 3},
            {'name': 'Python', 'category': 'technical', 'percentage': 90, 'icon_class': 'bx bxl-python', 'color': '#3776AB', 'order': 4},
            {'name': 'Django', 'category': 'technical', 'percentage': 85, 'icon_class': 'bx bxl-django', 'color': '#092E20', 'order': 5},
        ]
        
        for skill in tech_skills:
            obj, created = Skill.objects.get_or_create(
                name=skill['name'],
                category=skill['category'],
                defaults=skill
            )
            if created:
                self.stdout.write(f'✓ Created technical skill: {skill["name"]}')
        
        # Create Professional Skills
        prof_skills = [
            {'name': 'Communication', 'category': 'professional', 'percentage': 90, 'icon_class': 'bx bxs-chat', 'color': '#0ef', 'order': 1},
            {'name': 'Problem Solving', 'category': 'professional', 'percentage': 95, 'icon_class': 'bx bxs-brain', 'color': '#0ef', 'order': 2},
            {'name': 'Team Work', 'category': 'professional', 'percentage': 88, 'icon_class': 'bx bxs-group', 'color': '#0ef', 'order': 3},
            {'name': 'Creativity', 'category': 'professional', 'percentage': 85, 'icon_class': 'bx bxs-palette', 'color': '#0ef', 'order': 4},
        ]
        
        for skill in prof_skills:
            obj, created = Skill.objects.get_or_create(
                name=skill['name'],
                category=skill['category'],
                defaults=skill
            )
            if created:
                self.stdout.write(f'✓ Created professional skill: {skill["name"]}')
        
        # Create Services
        services = [
            {
                'title': 'Data Analysis',
                'description': 'Transform raw data into actionable insights with advanced analytics and visualization techniques.',
                'icon_class': 'bx bx-bar-chart-alt-2',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Machine Learning',
                'description': 'Build intelligent systems that learn from data and make predictions with high accuracy.',
                'icon_class': 'bx bx-brain',
                'order': 2,
                'is_active': True
            },
            {
                'title': 'AI Development',
                'description': 'Create cutting-edge AI solutions including NLP, computer vision, and generative AI.',
                'icon_class': 'bx bx-robot',
                'order': 3,
                'is_active': True
            },
            {
                'title': 'Web Development',
                'description': 'Build responsive and dynamic websites using Django, React, and modern technologies.',
                'icon_class': 'bx bx-code-alt',
                'order': 4,
                'is_active': True
            },
        ]
        
        for service in services:
            obj, created = Service.objects.get_or_create(
                title=service['title'],
                defaults=service
            )
            if created:
                self.stdout.write(f'✓ Created service: {service["title"]}')
        
        # Create Projects (without images to avoid errors)
        projects = [
            {
                'title': 'AI-Powered Chatbot',
                'description': 'An intelligent chatbot built with Python and NLP that understands context and provides accurate responses.',
                'technologies': 'Python, TensorFlow, NLTK, Django',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'E-commerce Analytics Dashboard',
                'description': 'Real-time analytics dashboard for e-commerce platforms with sales predictions and customer insights.',
                'technologies': 'Django, Chart.js, Pandas, PostgreSQL',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'Face Recognition System',
                'description': 'Advanced face recognition system for security applications with 98% accuracy.',
                'technologies': 'Python, OpenCV, FaceNet, Django',
                'order': 3,
                'is_featured': False
            },
        ]
        
        for project in projects:
            obj, created = Project.objects.get_or_create(
                title=project['title'],
                defaults=project
            )
            if created:
                self.stdout.write(f'✓ Created project: {project["title"]}')
            else:
                self.stdout.write(f'⚠ Project already exists: {project["title"]}')
        
        self.stdout.write(self.style.SUCCESS('\n✅ Sample data creation completed!'))
        self.stdout.write('\n📝 You can now:')
        self.stdout.write('  1. Go to http://127.0.0.1:8000/admin')
        self.stdout.write('  2. Login with your superuser credentials')
        self.stdout.write('  3. Add/edit projects, skills, services through the admin panel')
        self.stdout.write('  4. Upload images for projects (IMPORTANT: Add images to projects)')