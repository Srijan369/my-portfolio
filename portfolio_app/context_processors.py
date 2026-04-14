from .models import Profile, SocialLink

def global_data(request):
    """Context processor to make global data available to all templates"""
    try:
        profile = Profile.objects.first()
    except:
        profile = None
    
    social_links = SocialLink.objects.all()
    
    return {
        'global_profile': profile,
        'global_social_links': social_links,
    }