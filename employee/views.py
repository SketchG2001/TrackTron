from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth import logout
from .forms import RegistrationForm


def home(request):
    return render(request, 'employee/home.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
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
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            confirm_password = form.cleaned_data['confirm_password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']

            if password == confirm_password:
                if User.objects.filter(username=username).exists():
                    messages.info(request, 'Username already taken')
                    return redirect('register')
                elif User.objects.filter(email=email).exists():
                    messages.info(request, 'Email already exists')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password,
                                                    first_name=first_name, last_name=last_name)
                    user.save()
                    messages.success(request, 'User registered successfully. Please log in.')
                    return redirect('login')
            else:
                messages.error(request, "Password doesn't match")
                return redirect('register')
        else:
            messages.error(request, 'Invalid form submission. Please try again.')
            return redirect('register')
    else:
        form = RegistrationForm()
    return render(request, 'employee/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
