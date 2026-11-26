from django.urls import path
from . import views

urlpatterns = [
    path('', views.register, name='register'),
    path('apply-mentor/', views.mentor_register, name='mentor_register'),
    path('login/', views.login_view, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('logout/', views.logout_view, name='logout'),
]
