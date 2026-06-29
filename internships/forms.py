from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

from .models import Student, Application, Company, InternshipPosition

class StudentProfileForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            'roll_number', 'degree', 'branch', 'semester', 'gpa',
            'phone', 'skills', 'bio', 'linkedin_url',
            'profile_picture', 'resume',
        ]
        widgets = {
            'skills': forms.Textarea(attrs={'rows': 3, 'placeholder': 'e.g. Python, Django, React'}),
            'bio': forms.Textarea(attrs={'rows': 4}),
        }
 
    def clean_semester(self):
        semester = self.cleaned_data.get('semester')
        if semester is not None and not (1 <= semester <= 12):
            raise ValidationError('Enter a semester between 1 and 12.')
        return semester
 
    def clean_gpa(self):
        gpa = self.cleaned_data.get('gpa')
        # model field is max_digits=3, decimal_places=2 -> max storable value is 9.99
        if gpa is not None and not (0 <= gpa <= 9.99):
            raise ValidationError('GPA must be between 0 and 9.99.')
        return gpa