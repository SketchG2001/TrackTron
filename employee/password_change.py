from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.conf import settings
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from .models import Employee
from django.utils import timezone
from datetime import timedelta, datetime
import pyotp
from django.template.loader import render_to_string

def generate_otp():
    # Generate a 6-digit TOTP (Time-based One-Time Password)
    totp = pyotp.TOTP(pyotp.random_base32(), digits=6)
    otp = totp.now()
    expiry_time = timezone.now() + timedelta(minutes=5)
    return otp, expiry_time


def send_otp_email(user, otp):
    subject = 'Password Reset OTP'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    html_message = render_to_string('email/password_reset_otp.html', {'user': user, 'otp': otp})
    send_mail(subject, None, from_email, [to_email], html_message=html_message)


def send_password_change_request_received_email(user):
    subject = 'Password Change Request Received'
    message = f'Hello {user.username},\n\nWe have received a request to change your password.\n\nIf you initiated this request, please ignore this message.\n\nIf you did not request this change, please contact us immediately.\n\nBest regards,\nTrackTron Team'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email
    send_mail(subject, message, from_email, [to_email])


def change_password(request):
    if request.method == 'POST':
        form = PasswordResetForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            try:
                user = Employee.objects.get(email=email)
                otp,expiry_time  = generate_otp()  # Generate OTP
                send_otp_email(user, otp)  # Send OTP via email
                send_password_change_request_received_email(user)
                request.session['reset_user_id'] = user.id
                request.session['reset_otp'] = otp
                request.session['reset_otp_expiry'] = expiry_time.isoformat()
                # Redirect to OTP verification page
                uidb64 = urlsafe_base64_encode(bytes(str(user.id), 'utf-8'))
                token = default_token_generator.make_token(user)
                return redirect(reverse('verify_otp_and_reset_password', kwargs={'uidb64': uidb64, 'token': token}))

            except Employee.DoesNotExist:
                form.add_error('email', 'Employee does not exist.')
    else:
        form = PasswordResetForm()
    return render(request, 'employee/pass_reset.html', {'form': form})
