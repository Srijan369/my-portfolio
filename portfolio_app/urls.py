from django.urls import path
from . import views

app_name = 'portfolio_app'

urlpatterns = [
    # Single page - main portfolio
    path('', views.index, name='index'),
    
    # Project detail page (opens as separate page)
    path('project/<int:project_id>/', views.project_detail, name='project_detail'),
    
    # AJAX endpoint for contact form (optional)
    path('contact-ajax/', views.contact_ajax, name='contact_ajax'),
]