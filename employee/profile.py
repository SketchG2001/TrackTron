from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    username = request.user.first_name
    emp_id = request.user.id
    return render(request,'employee/profile.html',{'username':username,'emp_id':emp_id})