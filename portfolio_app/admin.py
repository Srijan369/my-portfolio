from django.contrib import admin
from django.utils.html import format_html
from django import forms
from .models import ContactMessage, Skill, Service, Project, Profile, SocialLink

# Custom form for Project to add helpful instructions
class ProjectAdminForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        help_texts = {
            'description': '''
            <div style="background: #f0f0f0; padding: 10px; border-radius: 5px; margin-top: 5px;">
                <strong>📝 You can use HTML formatting:</strong><br>
                • Use <code>&lt;strong&gt;text&lt;/strong&gt;</code> for <strong>bold text</strong><br>
                • Use <code>&lt;em&gt;text&lt;/em&gt;</code> for <em>italic text</em><br>
                • Use <code>&lt;ul&gt;&lt;li&gt;item&lt;/li&gt;&lt;/ul&gt;</code> for bullet points<br>
                • Use <code>&lt;h3&gt;Heading&lt;/h3&gt;</code> for subheadings<br>
                • Use <code>&lt;br&gt;</code> for line breaks<br>
                <strong>Example:</strong><br>
                <code>&lt;strong&gt;Key Features:&lt;/strong&gt;&lt;br&gt;
                &lt;ul&gt;
                &lt;li&gt;Feature 1&lt;/li&gt;
                &lt;li&gt;Feature 2&lt;/li&gt;
                &lt;/ul&gt;</code>
            </div>
            ''',
        }

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'email', 'subject', 'created_at', 'is_read', 'message_preview']
    list_filter = ['is_read', 'created_at']
    search_fields = ['name', 'email', 'message']
    readonly_fields = ['created_at']
    actions = ['mark_as_read', 'mark_as_unread']
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message Preview'
    
    def mark_as_read(self, request, queryset):
        updated = queryset.update(is_read=True)
        self.message_user(request, f'{updated} messages marked as read.')
    mark_as_read.short_description = "Mark selected messages as read"
    
    def mark_as_unread(self, request, queryset):
        updated = queryset.update(is_read=False)
        self.message_user(request, f'{updated} messages marked as unread.')
    mark_as_unread.short_description = "Mark selected messages as unread"

@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ['name', 'category', 'percentage', 'order', 'color_preview']
    list_filter = ['category']
    search_fields = ['name']
    list_editable = ['percentage', 'order']
    
    def color_preview(self, obj):
        return format_html(
            '<div style="width: 30px; height: 20px; background-color: {}; border-radius: 3px;"></div>',
            obj.color
        )
    color_preview.short_description = 'Color'

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'is_active', 'icon_preview']
    list_filter = ['is_active']
    search_fields = ['title', 'description']
    list_editable = ['order', 'is_active']
    
    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size: 20px;"></i>', obj.icon_class)
    icon_preview.short_description = 'Icon'

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    list_display = ['title', 'order', 'is_featured', 'image_preview', 'description_preview']
    list_filter = ['is_featured']
    search_fields = ['title', 'technologies', 'description']
    list_editable = ['order', 'is_featured']
    
    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 5px;" />',
                obj.image.url
            )
        return "No Image"
    image_preview.short_description = 'Image'
    
    def description_preview(self, obj):
        # Strip HTML tags for preview
        import re
        plain_text = re.sub(r'<[^>]+>', '', obj.description)
        return plain_text[:50] + '...' if len(plain_text) > 50 else plain_text
    description_preview.short_description = 'Description'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'description', 'image', 'project_url')
        }),
        ('Technical Details', {
            'fields': ('technologies',)
        }),
        ('Display Settings', {
            'fields': ('order', 'is_featured'),
            'classes': ('collapse',)
        }),
    )

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'email', 'phone']
    fieldsets = (
        ('Personal Information', {
            'fields': ('name', 'title', 'bio', 'profile_image')
        }),
        ('Contact Information', {
            'fields': ('email', 'phone', 'location')
        }),
        ('Resume', {
            'fields': ('resume_file',)
        })
    )
    
    def has_add_permission(self, request):
        # Only allow one profile
        if self.model.objects.count() >= 1:
            return False
        return super().has_add_permission(request)

@admin.register(SocialLink)
class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ['platform', 'url', 'order', 'icon_preview']
    search_fields = ['platform']
    list_editable = ['order']
    
    def icon_preview(self, obj):
        return format_html('<i class="{}" style="font-size: 20px;"></i>', obj.icon_class)
    icon_preview.short_description = 'Icon'