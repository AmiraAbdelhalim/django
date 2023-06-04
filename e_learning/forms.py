from django import forms
from .models import Student


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ('student_name', 'student_age',  'track',)
        widgets = {
            'student_name': forms.TextInput( attrs={'class': 'form-control '}),
            'student_age': forms.TextInput( attrs={'class': 'form-control '}),
            'track': forms.Select(attrs={'class': 'form-control '}),
        }
