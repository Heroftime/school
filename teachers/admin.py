from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from django.forms import ModelForm
from django.core.exceptions import ValidationError
from django.utils.html import format_html
from .models import Subject, Teacher
from .resources import TeacherResource


admin.site.register(Subject)
class TeacherForm(ModelForm):

    def clean(self):
        super(TeacherForm, self).clean()
        subjects = self.cleaned_data.get('subjects')
        
        if subjects.count() > 5:
            raise ValidationError({'subjects': ["Only five subjects are allowed at a time"]})


@admin.register(Teacher)
class TeacherAdmin(ImportExportModelAdmin):
    resource_class = TeacherResource
    search_fields = ('last_name', 'subjects__name')
    list_display = ['first_name', 'last_name', 'profile_page']
    form = TeacherForm

    def profile_page(self, obj):
        return format_html("<a href='{url}'>Teach</a>", url='/teacher/?id='+str(obj.id))

    profile_page.short_description = "Profile page"



class CustomAdminSite(admin.AdminSite):      
    def get_urls(self):        
        urls = super(CustomAdminSite, self).get_urls() 
        custom_urls = [            
            url(r'desired/path$', 
            self.admin_view(organization_admin.preview), name="preview"),        
        ]        
        return urls + custom_urls