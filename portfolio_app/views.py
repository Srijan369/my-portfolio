from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.views.decorators.http import require_POST
from .models import Skill, Service, Project, Profile, SocialLink, ContactMessage
from .forms import ContactForm

def index(request):
    """Single page view - renders all sections in one page"""
    
    # Get all data for the single page
    profile = Profile.objects.first()
    social_links = SocialLink.objects.all()
    services_list = Service.objects.filter(is_active=True)
    technical_skills = Skill.objects.filter(category='technical')
    professional_skills = Skill.objects.filter(category='professional')
    projects = Project.objects.all()
    
    # Handle contact form submission
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # Save to database
            contact_message = form.save()
            
            # Send email notification
            try:
                send_mail(
                    subject=f"Contact Form: {form.cleaned_data.get('subject', 'No Subject')}",
                    message=f"""
                    Name: {form.cleaned_data['name']}
                    Email: {form.cleaned_data['email']}
                    
                    Message:
                    {form.cleaned_data['message']}
                    """,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=[settings.EMAIL_HOST_USER],
                    fail_silently=True,
                )
            except Exception as e:
                print(f"Email error: {e}")
            
            messages.success(request, 'Thank you for your message! I will get back to you soon.')
            return redirect('portfolio_app:index')
        else:
            messages.error(request, 'Please correct the errors below.')
    else:
        form = ContactForm()
    
    context = {
        'profile': profile,
        'social_links': social_links,
        'services': services_list,
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'projects': projects,
        'form': form,
    }
    return render(request, 'portfolio_app/index.html', context)

def project_detail(request, project_id):
    """Individual project detail view - opens as separate page or modal"""
    project = get_object_or_404(Project, id=project_id)
    
    context = {
        'project': project,
    }
    return render(request, 'portfolio_app/project_detail.html', context)

# Helper view for AJAX contact form submission (optional)
@require_POST
def contact_ajax(request):
    """Handle AJAX contact form submission"""
    import json
    from django.http import JsonResponse
    
    form = ContactForm(request.POST)
    if form.is_valid():
        contact_message = form.save()
        
        try:
            send_mail(
                subject=f"Contact Form: {form.cleaned_data.get('subject', 'No Subject')}",
                message=f"""
                Name: {form.cleaned_data['name']}
                Email: {form.cleaned_data['email']}
                
                Message:
                {form.cleaned_data['message']}
                """,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
                fail_silently=True,
            )
        except:
            pass
        
        return JsonResponse({'success': True, 'message': 'Message sent successfully!'})
    else:
        errors = {field: error[0] for field, error in form.errors.items()}
        return JsonResponse({'success': False, 'errors': errors}, status=400)