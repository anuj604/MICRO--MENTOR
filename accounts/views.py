from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Profile
from mentors.models import Mentor, Booking

def register(request):
    """Student / Mentee Registration"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'error': 'Username already exists. Please choose another.'})

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role='student')

        # Auto-login student and redirect directly to Student Dashboard
        login(request, user)
        return redirect('/dashboard/')

    return render(request, 'register.html')

def mentor_register(request):
    """Mentor / Expert Application & Registration"""
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()
        skill = request.POST.get('skill', '').strip()
        experience = request.POST.get('experience', '1').strip()
        expertise = request.POST.get('expertise', '').strip()
        phone = request.POST.get('phone', '').strip()

        if User.objects.filter(username=username).exists():
            return render(request, 'mentor_register.html', {
                'error': 'Username already exists. Please choose another.',
                'skill': skill,
                'experience': experience,
                'expertise': expertise,
                'phone': phone
            })

        try:
            exp_int = int(experience)
        except ValueError:
            exp_int = 1

        user = User.objects.create_user(username=username, password=password)
        Profile.objects.create(user=user, role='mentor')
        Mentor.objects.create(
            user=user,
            skill=skill,
            experience=exp_int,
            expertise=expertise,
            phone=phone,
            is_available=True
        )

        # Auto-login mentor and redirect directly to Mentor Dashboard!
        login(request, user)
        return redirect('/mentor/dashboard/')

    return render(request, 'mentor_register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        password = request.POST.get('password', '').strip()

        user = authenticate(request, username=username, password=password)

        if user:
            login(request, user)

            try:
                profile = Profile.objects.get(user=user)
                if profile.role == 'mentor':
                    return redirect('/mentor/dashboard/')
                else:
                    return redirect('/dashboard/')
            except Profile.DoesNotExist:
                return redirect('/dashboard/')

        else:
            return render(request, 'login.html', {'error': 'Invalid username or password.'})

    return render(request, 'login.html')

@login_required
def dashboard(request):
    bookings = Booking.objects.filter(student=request.user).order_by('-id')
    total_bookings = bookings.count()
    pending_bookings = bookings.filter(status='pending').count()
    accepted_bookings = bookings.filter(status='accepted').count()
    recent_bookings = bookings[:4]

    available_mentors = Mentor.objects.filter(is_available=True)[:3]
    total_mentors = Mentor.objects.filter(is_available=True).count()

    return render(request, 'dashboard.html', {
        'total_bookings': total_bookings,
        'pending_bookings': pending_bookings,
        'accepted_bookings': accepted_bookings,
        'recent_bookings': recent_bookings,
        'available_mentors': available_mentors,
        'total_mentors': total_mentors,
    })

def logout_view(request):
    logout(request)
    return redirect('login')
