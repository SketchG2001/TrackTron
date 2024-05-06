# dashboard.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    username = request.user.first_name
    emp_id = request.user.id
    print(username)
    return render(request, 'employee/dashboard.html',{'username':username,'emp_id':emp_id})