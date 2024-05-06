from django.contrib.auth.models import User
from django import forms

class RegistrationForm(forms.Form):

    first_name = forms.CharField(label='First Name', min_length=3, max_length=50)
    last_name = forms.CharField(label='Last Name', min_length=3, max_length=50)
    username = forms.CharField(label='Username', min_length=3, max_length=50)
    email = forms.EmailField(label='Email', min_length=3, max_length=50)
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirm Password', widget=forms.PasswordInput)


    # name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'placeholder': 'Enter your name'}))
    # email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Enter your email'}))
    # mobile = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'placeholder': 'Enter your mobile number'}))
    # DOB = forms.DateField(widget=forms.TextInput(attrs={'placeholder': 'YYYY-MM-DD', 'class': 'form-control', 'type': 'date'}), input_formats=['%Y-%m-%d'])
    # bloodgroup = forms.ChoiceField(choices=[
    #     ('A+', 'A+'),
    #     ('A-', 'A-'),
    #     ('B+', 'B+'),
    #     ('B-', 'B-'),
    #     ('O+', 'O+'),
    #     ('O-', 'O-'),
    #     ('AB+', 'AB+'),
    #     ('AB-', 'AB-'),
    # ], widget=forms.Select(attrs={'placeholder': 'Select your blood group'}))
    # department = forms.ChoiceField(choices=[
    #     ('IT', 'Information Technology'),
    #     ('CS', 'Computer Science'),
    #     ('ECE', 'Electronics and Communication Engineering'),
    #     # Add more choices as needed
    # ], widget=forms.Select(attrs={'placeholder': 'Select your department'}))
    # password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Enter your password'}))
    # password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Confirm your password'}))

class LoginForm(forms.Form):
    email = forms.EmailField(label='Email')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)

