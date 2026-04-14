from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    """Enhanced contact form with better validation"""
    
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Enter Your Name',
                'required': True,
                'class': 'form-control'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'Enter Your Email',
                'required': True,
                'class': 'form-control'
            }),
            'subject': forms.TextInput(attrs={
                'placeholder': 'Enter Your Subject',
                'class': 'form-control'
            }),
            'message': forms.Textarea(attrs={
                'placeholder': 'Enter Your Message',
                'cols': 40,
                'rows': 10,
                'required': True,
                'class': 'form-control'
            }),
        }
    
    def clean_name(self):
        """Validate name field"""
        name = self.cleaned_data.get('name')
        if not name or len(name.strip()) < 2:
            raise forms.ValidationError('Name must be at least 2 characters long')
        if len(name) > 100:
            raise forms.ValidationError('Name is too long (max 100 characters)')
        if any(char.isdigit() for char in name):
            raise forms.ValidationError('Name should not contain numbers')
        return name.strip()
    
    def clean_email(self):
        """Validate email field"""
        email = self.cleaned_data.get('email')
        if not email:
            raise forms.ValidationError('Email is required')
        
        # Additional email validation
        import re
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not re.match(email_pattern, email):
            raise forms.ValidationError('Please enter a valid email address')
        
        return email.lower()
    
    def clean_subject(self):
        """Validate subject field (optional)"""
        subject = self.cleaned_data.get('subject', '')
        if subject and len(subject) > 200:
            raise forms.ValidationError('Subject is too long (max 200 characters)')
        return subject.strip() if subject else ''
    
    def clean_message(self):
        """Validate message field"""
        message = self.cleaned_data.get('message')
        if not message or len(message.strip()) < 10:
            raise forms.ValidationError('Message must be at least 10 characters long')
        if len(message) > 5000:
            raise forms.ValidationError('Message is too long (max 5000 characters)')
        
        # Check for spam patterns
        spam_keywords = ['viagra', 'casino', 'lottery', 'prize', 'winner']
        message_lower = message.lower()
        for keyword in spam_keywords:
            if keyword in message_lower:
                raise forms.ValidationError('Your message contains inappropriate content')
        
        return message.strip()
    
    def clean(self):
        """Global form validation"""
        cleaned_data = super().clean()
        
        # Check for empty fields
        if not cleaned_data.get('name'):
            self.add_error('name', 'Name is required')
        if not cleaned_data.get('email'):
            self.add_error('email', 'Email is required')
        if not cleaned_data.get('message'):
            self.add_error('message', 'Message is required')
        
        return cleaned_data