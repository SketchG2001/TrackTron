from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_decode
from django.contrib.auth import authenticate, login
from django.http import Http404
from .forms import OTPVerificationForm, NewPasswordForm
from .models import Employee
from django.core.mail import send_mail
from django.conf import settings
from django.utils import timezone
from datetime import datetime

def verify_otp_and_reset_password(request, uidb64, token):
    try:
        # Decode uidb64 to get the user's primary key
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Employee.objects.get(pk=uid)
        # Validate the token
        if default_token_generator.check_token(user, token):
            if request.method == 'POST':
                form = OTPVerificationForm(request.POST)
                if form.is_valid():
                    entered_otp = form.cleaned_data['otp']
                    session_otp = request.session.get('reset_otp')
                    saved_expiry_time = request.session.get('reset_otp_expiry')
                    expiry_time = datetime.fromisoformat(saved_expiry_time)
                    if entered_otp == session_otp and timezone.now() <= expiry_time:
                        request.session['uid'] = uid  # Store uid in session
                        return redirect('new_password')
                    else:
                        messages.error(request, 'Invalid or expired OTP. Please try again.')
                        return redirect('password_change')
            else:
                form = OTPVerificationForm()

            return render(request, 'employee/otp_verification.html', {'form': form})
        else:
            return render(request, 'employee/invalid_token.html')

    except (TypeError, ValueError, OverflowError, Employee.DoesNotExist):
        return render(request, 'employee/invalid_token.html')


def send_password_changed_email(user):
    subject = 'Password Changed Successfully'
    message = f'Hello {user.username},\n\nYour password has been changed successfully.\n\nIf you did not request this change, please contact us immediately.\n\nBest regards,\nTrackTron Team'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message, from_email, [to_email])


def new_password(request):
    if request.method == 'POST':
        form = NewPasswordForm(request.POST)
        if form.is_valid():
            new_password = form.cleaned_data['new_password']
            confirm_new_password = form.cleaned_data['confirm_new_password']
            uid = request.session.get('uid')  # Retrieve uid from session
            if uid:
                try:
                    user = Employee.objects.get(pk=uid)
                    if new_password == confirm_new_password:
                        # Set new password and authenticate user
                        user.set_password(new_password)
                        user.save()
                        send_password_changed_email(user)
                        user = authenticate(request, username=user.username, password=new_password)
                        if user is not None:
                            login(request, user)
                            return redirect('dashboard')
                except Employee.DoesNotExist:
                    raise Http404("User does not exist.")  # Handle user not found
        # If form is not valid or user not authenticated, render the form again
    else:
        form = NewPasswordForm()

    return render(request, 'employee/new_password.html', {'form': form})
