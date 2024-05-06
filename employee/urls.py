from django.urls import path
from . import views
from .dashboard import dashboard
from .presence import presence

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout', views.logout_view, name='logout'),
    path('presence', presence, name='presence'),
]
