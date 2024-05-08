from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def leave_req(request):
    username = request.user.first_name
    emp_id = request.user.id
    return render(request,'employee/leave_req.html',{'username':username,'emp_id':emp_id})