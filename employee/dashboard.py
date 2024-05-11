# dashboard.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from employee.models import LeaveRequest


@login_required
def dashboard(request):
    user = request.user
    leave_requests = LeaveRequest.objects.filter(employee=user)

    context = {
        'user': user,
        'leave_requests': leave_requests
    }
    return render(request, 'employee/dashboard.html', context)