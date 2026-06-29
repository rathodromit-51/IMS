from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name', 'location', 'email']
    search_fields = ['name', 'location']
    list_filter = ['location', 'created_at']
    
    
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['roll_number', 'user', 'degree', 'semester', 'gpa']
    search_fields = ['roll_number', 'user__first_name']
    list_filter = ['degree', 'semester']
    

@admin.register(InternshipPosition)
class InternshipPositionAdmin(admin.ModelAdmin):
    list_display = ['title', 'company', 'location', 'status', 'duration_weeks']
    search_fields = ['title', 'company__name']
    list_filter = ['status', 'company', 'location']
    
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ['student', 'position', 'status', 'applied_on']
    search_fields =  ['student__user__first_name', 'position__title']
    list_filter = ['status', 'applied_on']
    


