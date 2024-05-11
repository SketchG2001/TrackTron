from django.shortcuts import render
from django.contrib.auth.decorators import login_required


# 22.6876, 75.827124
# 22.7049472, 75.9005184
# 22.6876039, 75.8271282
@login_required
def presence(request):
    username = request.user.username
    name = request.user.name
    emp_id = request.user.id
    return render(request, 'employee/presence.html', {'name': name, 'username': username, 'emp_id': emp_id})
