from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, LeaveRequest
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


def send_email(user, page, subject):
    subject = f'{subject}'
    from_email = settings.EMAIL_HOST_USER
    to_email = user.email

    # Render HTML email content using a template
    html_message = render_to_string(f'email/{page}.html', {'user': user})

    # Create EmailMultiAlternatives instance for sending HTML email
    email = EmailMultiAlternatives(subject, body=None, from_email=from_email, to=[to_email])
    email.attach_alternative(html_message, "text/html")  # Attach HTML content as alternative

    try:
        email.send()  # Send the email
        return True  # Email sent successfully
    except Exception as e:
        print(f"Error sending email: {e}")
        return False  # Email sending failed


def is_superuser(user):
    return user.is_superuser


@login_required
# @user_passes_test(is_superuser)
def hradmin(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    employees = Employee.objects.filter(is_staff=True, is_superuser=False)

    return render(request, 'hradmin/employee_list.html', {'employees': employees})


@login_required
def new_employee(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    new_user = Employee.objects.filter(is_active=False)
    return render(request, 'hradmin/newemp.html', {'new_user': new_user})


@login_required
def approve_employee(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    user = get_object_or_404(Employee, id=user_id)
    user.is_staff = True
    user.is_active = True
    user.save()
    if user.is_staff and user.is_active:
        if send_email(user, 'account_approved', 'account_approved'):
            messages.success(request, 'Account approved and email sent.')
            return redirect('hradmin')


@login_required
def reject_employee(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    employe = get_object_or_404(Employee, id=user_id)
    print(employe.email)
    employe.delete()
    return redirect('hradmin')


@login_required
def new_emp_count(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    new_emp = Employee.objects.filter(is_active=False).count()
    new_leave = LeaveRequest.objects.filter(status='pending').count()
    return JsonResponse({'new_emp': new_emp,'new_leave': new_leave})


@login_required
def delete_emp(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    emp = get_object_or_404(Employee, id=user_id)
    emp.is_staff = False
    emp.save()
    messages.success(request, f'{emp.name} has been deactivated successfully.')
    return redirect('hradmin')


@login_required
def view_leave_requests(request):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to access this page.')
        return redirect('dashboard')  # Redirect to a suitable page if not admin
    pending_requests = LeaveRequest.objects.filter(status='pending')
    return render(request, 'hradmin/leave_approval.html', {'pending_requests': pending_requests})


@login_required
def approve_leave(request, request_id):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to approve leave requests.')
        return redirect('logout')
    leave_request = get_object_or_404(LeaveRequest, pk=request_id)
    leave_request.status = 'approved'
    leave_request.save()
    emp_id = leave_request.employee_id
    user = get_object_or_404(Employee, id=emp_id)
    send_email(user, 'leave_appro', 'Your Leave has been approved.')
    messages.success(request, 'Leave request approved successfully.')
    return redirect('view_leave_requests')


@login_required
def reject_leave(request, request_id):
    if not request.user.is_superuser:
        messages.error(request, 'You are not authorized to reject leave requests.')
        return redirect('logout')
    leave_request = get_object_or_404(LeaveRequest, pk=request_id)
    leave_request.status = 'rejected'
    leave_request.save()
    messages.success(request, 'Leave request rejected successfully.')
    return redirect('view_leave_requests')

# reshma9624
