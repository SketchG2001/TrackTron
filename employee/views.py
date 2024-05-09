
from django.contrib.auth.hashers import make_password
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm,CustomAuthenticationForm

def home(request):
    return render(request, 'employee/home.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('hradmin')
                else:
                    return redirect('dashboard')
            # Replace 'dashboard' with your actual URL name
            else:
                form.add_error(None, "Invalid username or password.")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'employee/login.html', {'form': form})



def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            clear_pass = form.cleaned_data['password']
            hashed_pass = make_password(clear_pass)
            # Update the user's password with the hashed value
            user = form.save(commit=False)
            user.password = hashed_pass
            user.save()
            messages.success(request, 'You have been registered successfully.')
            return redirect('login')  # Replace 'login' with your actual URL name
        else:
            print("Form is not valid")
            print(form.errors)  # Print form errors for debugging
    else:
        form = SignUpForm()

    return render(request, 'employee/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('login')
