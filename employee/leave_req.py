from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LeaveRequestForm
from .models import LeaveRequest


@login_required
def leave_request_create(request):
    if request.user.is_superuser:
        messages.error(request, 'You cannot request leaves using superuser account please login with your employee account')
        return redirect('logout')
    existing_pending_requests = LeaveRequest.objects.filter(employee=request.user, status='pending').exists()
    if existing_pending_requests:
        messages.error(request, 'You already have a pending leave request. Please wait for it to be processed.')
        return redirect('dashboard')
    if request.method == 'POST':
        form = LeaveRequestForm(request.POST)
        if form.is_valid():
            leave_request = form.save(commit=False)
            leave_request.employee = request.user
            leave_request.status = 'pending'
            leave_request.save()
            messages.success(request, 'Leave request submitted successfully.')
            return redirect('dashboard')
    else:
        form = LeaveRequestForm()
    return render(request, 'employee/leave_req.html', {'form': form})
