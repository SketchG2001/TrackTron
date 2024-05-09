# dashboard.py
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    user = request.user
    username = user.name
    name = user.name
    emp_id = user.id
    department = user.department
    blood_group = user.blood_group
    dob = user.dob
    age_years = user.age_years
    mobile = user.mobile
    email = user.email
    gender = user.gender
    last_login = user.last_login
    print(emp_id)
    return render(request, 'employee/dashboard.html',{
        'name':name,
        'username': username,
        'emp_id': emp_id,
        'department': department,
        'blood_group': blood_group,
        'dob': dob,
        'age_years': age_years,
        'mobile': mobile,
        'gender': gender,
        'last_login' : last_login,
        'email': email,
    })