import re
from datetime import datetime, timedelta
from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse
from .forms import SignUpForm

from employee.models import Employee


def home(request):
    return render(request, 'employee/home.html')


def login_view(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        print(email)
        print(password)
        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'Invalid Credentials')
            return redirect('login')
    else:
        return render(request, 'employee/login.html')


def register(request):
    if request.method == 'POST':
        print("post request")
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Access form data directly from cleaned_data
            print("form is valid")
            name = form.cleaned_data.get('name')
            department = form.cleaned_data.get('department')
            blood_group = form.cleaned_data.get('blood_group')
            dob = form.cleaned_data.get('dob')
            age = form.cleaned_data.get('age_years')
            mobile = form.cleaned_data.get('mobile')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            gender = form.cleaned_data.get('gender')


            print(name, department, blood_group, dob, mobile, email, password, gender,age)

            # Save the form data
            form.save()

            # Redirect to a success page or URL
            return redirect('login')  # Replace 'success_url' with your actual URL
        else:
            print("Form is not valid")
            print(form.errors)  # Print form errors for debugging
    else:
        form = SignUpForm()

    return render(request, 'employee/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
