from django.urls import path
from . import views
from .dashboard import dashboard
from .presence import presence
from .reports import reports
from .leave_req import leave_request_create
from .profile import profile
from .hradmin import (hradmin,new_employee,approve_employee,
                      reject_employee,new_emp_count,delete_emp,
                      view_leave_requests,approve_leave,reject_leave)

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    path('presence', presence, name='presence'),
    path('reports', reports, name='reports'),
    path('leave', leave_request_create, name='leave'),
    path('profile', profile, name='profile'),
    path('hradmin', hradmin, name='hradmin'),
    path('new_employee', new_employee, name='new_employee'),
    path('approve-employee/<int:user_id>/', approve_employee, name='approve_employee'),
    path('reject_employee/<int:user_id>/', reject_employee, name='reject_employee'),
    path('new_emp_count', new_emp_count, name='new_emp_count'),
    path('delete_emp/<int:user_id>/', delete_emp, name='delete_emp'),
    path('view_leave_requests/', view_leave_requests, name='view_leave_requests'),
    path('approve_leave/<int:request_id>/', approve_leave, name='approve_leave'),
    path('reject_leave/<int:request_id>/', reject_leave, name='reject_leave'),

]
