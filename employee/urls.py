from django.urls import path
from . import views
from .dashboard import dashboard
from .presence import presence
from .reports import reports
from .leave_req import leave_req
from .profile import profile
from .hradmin import hradmin,new_employee,approve_employee_view

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    path('presence', presence, name='presence'),
    path('reports', reports, name='reports'),
    path('leave', leave_req, name='leave'),
    path('profile', profile, name='profile'),
    path('hradmin', hradmin, name='hradmin'),
    path('new_employee', new_employee, name='new_employee'),
path('approve-employee/<int:user_id>/', approve_employee_view, name='approve_employee'),
]
