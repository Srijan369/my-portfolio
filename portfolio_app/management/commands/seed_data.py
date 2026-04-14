from django.core.management.base import BaseCommand
from portfolio_app.models import Profile, SocialLink, Skill, Service, Project
from django.core.files.base import ContentFile
import os

class Command(BaseCommand):
    help = 'Seed initial data for portfolio'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding initial data...')
        
        # Create Profile
        profile, created = Profile.objects.get_or_create(
            name='Shiva',
            defaults={
                'title': 'AI Developer',
                'bio': '''I am an Artificial Intelligence Developer with a strong foundation in Python and Data Science.
My work focuses on designing and implementing intelligent systems to solve complex problems.
I have hands-on experience in machine learning, deep learning, and predictive analytics.
I am passionate about transforming data into meaningful insights through AI-driven solutions.
My approach combines technical expertise with a problem-solving mindset.
I continuously strive to learn emerging technologies and apply them effectively.
My objective is to contribute to innovative projects that create real-world impact.''',
                'email': 'shiva@example.com',
                'phone': '+91 9876543210',
                'location': 'Varanasi, India'
            }
        )
        self.stdout.write(f'Profile: {"Created" if created else "Already exists"}')
        
        # Create Social Links
        social_links = [
            {'platform': 'GitHub', 'url': 'https://github.com/shiva', 'icon_class': 'bx bxl-github', 'order': 1},
            {'platform': 'LinkedIn', 'url': 'https://linkedin.com/in/shiva', 'icon_class': 'bx bxl-linkedin', 'order': 2},
            {'platform': 'Twitter', 'url': 'https://twitter.com/shiva', 'icon_class': 'bx bxl-twitter', 'order': 3},
            {'platform': 'Instagram', 'url': 'https://instagram.com/shiva', 'icon_class': 'bx bxl-instagram', 'order': 4},
            {'platform': 'Facebook', 'url': 'https://facebook.com/shiva', 'icon_class': 'bx bxl-facebook', 'order': 5},
            {'platform': 'YouTube', 'url': 'https://youtube.com/@shiva', 'icon_class': 'bx bxl-youtube', 'order': 6},
        ]
        
        for link in social_links:
            obj, created = SocialLink.objects.get_or_create(**link)
            if created:
                self.stdout.write(f'Created social link: {link["platform"]}')
        
        # Create Technical Skills
        technical_skills = [
            {'name': 'HTML', 'category': 'technical', 'percentage': 73, 'icon_class': 'bx bxl-html5', 'color': '#E34C26', 'order': 1},
            {'name': 'CSS', 'category': 'technical', 'percentage': 78, 'icon_class': 'bx bxl-css3', 'color': '#6924b3', 'order': 2},
            {'name': 'JavaScript', 'category': 'technical', 'percentage': 60, 'icon_class': 'bx bxl-javascript', 'color': '#F7DF1E', 'order': 3},
            {'name': 'Python', 'category': 'technical', 'percentage': 93, 'icon_class': 'bx bxl-python', 'color': '#3d6998', 'order': 4},
            {'name': 'SQL', 'category': 'technical', 'percentage': 90, 'icon_class': 'bx bxl-postgresql', 'color': '#f29111', 'order': 5},
        ]
        
        for skill in technical_skills:
            obj, created = Skill.objects.get_or_create(
                name=skill['name'],
                defaults=skill
            )
            if created:
                self.stdout.write(f'Created technical skill: {skill["name"]}')
        
        # Create Professional Skills
        professional_skills = [
            {'name': 'Creativity', 'category': 'professional', 'percentage': 90, 'icon_class': 'bx bxs-palette', 'color': '#0ef', 'order': 1},
            {'name': 'Communication', 'category': 'professional', 'percentage': 85, 'icon_class': 'bx bxs-chat', 'color': '#0ef', 'order': 2},
            {'name': 'Problem Solving', 'category': 'professional', 'percentage': 95, 'icon_class': 'bx bxs-brain', 'color': '#0ef', 'order': 3},
            {'name': 'Team Work', 'category': 'professional', 'percentage': 93, 'icon_class': 'bx bxs-group', 'color': '#0ef', 'order': 4},
        ]
        
        for skill in professional_skills:
            obj, created = Skill.objects.get_or_create(
                name=skill['name'],
                defaults=skill
            )
            if created:
                self.stdout.write(f'Created professional skill: {skill["name"]}')
        
        # Create Services
        services = [
            {
                'title': 'Data Analysis',
                'description': 'Expert in data analysis, visualization, and interpretation. Transforming raw data into actionable insights for business growth using Python, Pandas, and advanced analytics techniques.',
                'icon_class': 'bx bx-code',
                'order': 1,
                'is_active': True
            },
            {
                'title': 'Machine Learning',
                'description': 'Building intelligent ML models for predictive analytics, classification, and pattern recognition using advanced algorithms like Random Forest, XGBoost, and Neural Networks.',
                'icon_class': 'bx bx-crop',
                'order': 2,
                'is_active': True
            },
            {
                'title': 'AI Solutions',
                'description': 'Developing cutting-edge AI solutions including NLP, computer vision, and generative AI applications using TensorFlow, PyTorch, and Hugging Face.',
                'icon_class': 'bx bxl-apple',
                'order': 3,
                'is_active': True
            },
            {
                'title': 'Data Science',
                'description': 'Comprehensive data science services including data preprocessing, feature engineering, model deployment, and creating interactive dashboards with Streamlit and Django.',
                'icon_class': 'bx bxs-ghost',
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
                self.stdout.write(f'Created service: {service["title"]}')
        
        # Create Projects
        projects = [
            {
                'title': 'AI Chatbot Development',
                'description': 'Developed an intelligent chatbot using Python and NLP for customer service automation with 95% accuracy. Implemented using Transformer models and deployed on cloud.',
                'technologies': 'Python, TensorFlow, NLTK, Flask',
                'order': 1,
                'is_featured': True
            },
            {
                'title': 'Predictive Analytics Dashboard',
                'description': 'Created an interactive dashboard for sales prediction using machine learning algorithms and real-time data visualization. Features include real-time updates and export functionality.',
                'technologies': 'Python, Pandas, Scikit-learn, Django, Chart.js',
                'order': 2,
                'is_featured': True
            },
            {
                'title': 'Computer Vision System',
                'description': 'Built a real-time object detection system using deep learning for security and surveillance applications. Achieved 92% accuracy on custom dataset.',
                'technologies': 'Python, OpenCV, YOLO, CNN, PyTorch',
                'order': 3,
                'is_featured': True
            },
        ]
        
        for project in projects:
            obj, created = Project.objects.get_or_create(
                title=project['title'],
                defaults=project
            )
            if created:
                self.stdout.write(f'Created project: {project["title"]}')
        
        self.stdout.write(self.style.SUCCESS('✅ Successfully seeded all initial data!'))