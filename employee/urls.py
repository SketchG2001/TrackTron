from django.urls import path
from . import views
from .dashboard import dashboard, profile_picture
from .presence import presence
from .reports import reports, all_employees, download_reports_csv
from .leave_req import leave_request_create
from .profile import profile
from .hradmin import (hradmin, new_employee, approve_employee,
                      reject_employee, new_emp_count, delete_emp,
                      view_leave_requests, approve_leave, reject_leave)
from .password_change import change_password
from django.contrib.auth import views as auth_views
from .verify_otp import verify_otp_and_reset_password, new_password
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login_view, name='login'),
    path('register', views.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('profile_picture/', profile_picture, name='profile_picture'),
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
    path('all_employees', all_employees, name='employee_reports'),
    path('download-reports-csv/', download_reports_csv, name='download_reports_csv'),
    path('password_change/', change_password, name='password_change'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset/verify/<uidb64>/<token>/', verify_otp_and_reset_password,
         name='verify_otp_and_reset_password'),
    path('new_password/', new_password, name='new_password'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
