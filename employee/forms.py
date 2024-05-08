from django import forms
from .models import Employee
import re

class SignUpForm(forms.ModelForm):
    DEPARTMENT_CHOICES = [
        ('CS', 'Computer Science'),
        ('IT', 'Information Technology'),
        ('HR', 'Human Resources'),
        ('Library', 'Library'),
        ('Admission', 'Admission'),
    ]

    BLOOD_GROUP_CHOICES = [
        ('A+', 'A+'),
        ('A-', 'A-'),
        ('B+', 'B+'),
        ('B-', 'B-'),
        ('AB+', 'AB+'),
        ('AB-', 'AB-'),
        ('O+', 'O+'),
        ('O-', 'O-'),
    ]

    department = forms.ChoiceField(choices=DEPARTMENT_CHOICES)
    blood_group = forms.ChoiceField(choices=BLOOD_GROUP_CHOICES)
    confirm_password = forms.CharField(max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = Employee
        fields = '__all__'

    def clean(self):
        cleaned_data = super().clean()
        errors = {}

        name = cleaned_data.get('name')
        if not name:
            errors['name'] = "Name is required."
        elif not re.match(r'^[a-zA-Z]+(?: [a-zA-Z]+)*$', name):
            errors['name'] = "Name must contain only letters and spaces."

        dob = cleaned_data.get('dob')
        if not dob:
            errors['dob'] = "Date of Birth is required."

        age_years = cleaned_data.get('age_years')
        if age_years and age_years < 18:
            errors['age_years'] = "Employee age must be greater than 18."

        mobile = cleaned_data.get('mobile')
        if not mobile:
            errors['mobile'] = "Mobile number is required."
        elif not re.match(r'^[0-9]{10,14}$', mobile):
            errors['mobile'] = "Invalid mobile number."

        email = cleaned_data.get('email')
        if not email:
            errors['email'] = "Email is required."
        elif not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email):
            errors['email'] = "Invalid email address."

        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        if not password:
            errors['password'] = "Password is required."
        elif len(password) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        elif password != confirm_password:
            errors['confirm_password'] = "Passwords do not match."

        gender = cleaned_data.get('gender')
        if gender not in ['male', 'female']:
            errors['gender'] = "Invalid gender."

        if errors:
            raise forms.ValidationError(errors)

        return cleaned_data
