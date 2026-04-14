from django.db import models
from django.utils import timezone
from django.core.validators import MinLengthValidator, EmailValidator

class ContactMessage(models.Model):
    """Model for storing contact form submissions"""
    name = models.CharField(max_length=100, validators=[MinLengthValidator(2)])
    email = models.EmailField(validators=[EmailValidator()])
    subject = models.CharField(max_length=200, blank=True)
    message = models.TextField(validators=[MinLengthValidator(10)])
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'
    
    def __str__(self):
        return f"{self.name} - {self.created_at.strftime('%Y-%m-%d %H:%M')}"

class Skill(models.Model):
    """Model for technical skills"""
    SKILL_CATEGORIES = [
        ('technical', 'Technical'),
        ('professional', 'Professional'),
    ]
    
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=20, choices=SKILL_CATEGORIES)
    percentage = models.IntegerField(default=0, help_text="Skill proficiency percentage")
    icon_class = models.CharField(max_length=50, help_text="Boxicons class name")
    color = models.CharField(max_length=20, default='#00eeff')
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.name

class Service(models.Model):
    """Model for services offered"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon_class = models.CharField(max_length=50, help_text="Boxicons class name")
    order = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title

class Project(models.Model):
    """Model for portfolio projects"""
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/')
    project_url = models.URLField(blank=True)
    technologies = models.CharField(max_length=200, help_text="Comma-separated technologies")
    order = models.IntegerField(default=0)
    is_featured = models.BooleanField(default=False)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.title
    
    def get_technologies_list(self):
        return [tech.strip() for tech in self.technologies.split(',')]

class Profile(models.Model):
    """Model for profile information"""
    name = models.CharField(max_length=100, default='Shiva')
    title = models.CharField(max_length=100, default='AI Developer')
    bio = models.TextField()
    profile_image = models.ImageField(upload_to='profile/')
    resume_file = models.FileField(upload_to='resume/', blank=True)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    location = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = 'Profile'
        verbose_name_plural = 'Profile'
    
    def __str__(self):
        return self.name

class SocialLink(models.Model):
    """Model for social media links"""
    platform = models.CharField(max_length=50)
    url = models.URLField()
    icon_class = models.CharField(max_length=50)
    order = models.IntegerField(default=0)
    
    class Meta:
        ordering = ['order']
    
    def __str__(self):
        return self.platform