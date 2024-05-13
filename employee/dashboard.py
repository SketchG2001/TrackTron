import os
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from employee.models import LeaveRequest
from tracktron import settings
from .forms import ProfilePictureForm


@login_required
def dashboard(request):
    user = request.user
    leave_requests = LeaveRequest.objects.filter(employee=user)
    context = {
        'user': user,
        'leave_requests': leave_requests
    }
    return render(request, 'employee/dashboard.html', context)


@login_required
def profile_picture(request):
    user = request.user
    if request.method == 'POST':
        form = ProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            profile_pic = form.cleaned_data['profile_pic']
            if user.profile_picture:
                # Delete the existing profile picture file
                existing_pic_path = os.path.join(settings.MEDIA_ROOT, str(user.profile_picture))
                if os.path.exists(existing_pic_path):
                    os.remove(existing_pic_path)

            # Save the new profile picture
            user.profile_picture = profile_pic
            user.save()
            messages.success(request, 'Your profile picture has been updated.')
            return redirect('dashboard')
    else:
        form = ProfilePictureForm()
    return render(request, 'employee/dashboard.html', {'form': form})
