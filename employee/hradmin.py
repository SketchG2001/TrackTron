from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Employee, LeaveRequest
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse
from django.contrib.auth.models import User


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
    return redirect('hradmin')


@login_required
def reject_employee(request, user_id):
    if not request.user.is_superuser:
        return redirect('dashboard')
    employe = get_object_or_404(Employee, id=user_id)
    employe.delete()
    return redirect('hradmin')


@login_required
def new_emp_count(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    new_emp = Employee.objects.filter(is_active=False).count()
    return JsonResponse({'new_emp': new_emp})


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
