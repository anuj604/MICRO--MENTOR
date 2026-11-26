from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.mentor_dashboard, name='mentor_dashboard'),
    path('mentors/', views.mentor_list, name='mentor_list'),
    path('book/<int:mentor_id>/', views.book_mentor, name='book_mentor'),
    path('my-bookings/', views.my_bookings, name='my_bookings'),
    path('accept/<int:id>/', views.accept_booking, name='accept_booking'),
    path('reject/<int:id>/', views.reject_booking, name='reject_booking'),
    path('cancel/<int:id>/', views.cancel_booking, name='cancel_booking'),
    path('toggle-availability/', views.toggle_availability, name='toggle_availability'),
]
