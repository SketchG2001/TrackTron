from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from django.contrib.auth.decorators import login_required, user_passes_test
from django.http import JsonResponse


def is_superuser(user):
    return user.is_superuser


@login_required
# @user_passes_test(is_superuser)
def hradmin(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    employees = Employee.objects.filter(is_staff=True)
    supru = request.user.is_superuser
    return render(request, 'hradmin/employee_list.html', {'employees': employees,'supru': supru})


@login_required
def new_employee(request):
    if not request.user.is_superuser:
        return redirect('dashboard')
    new_user = Employee.objects.filter(is_staff=False)
    supru = request.user.is_superuser

    return render(request, 'hradmin/newemp.html', {'new_user': new_user, 'supru': supru})

@login_required
def approve_employee_view(request,user_id):

    if request.method == 'POST' and request.is_ajax():
        try:
            # Get user instance and update fields
            user = Employee.objects.get(pk=user_id)
            user.is_active = True
            user.is_staff = True
            user.save()
            return JsonResponse({'success': True})
        except Employee.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Employee not found'})
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method or not AJAX'})
