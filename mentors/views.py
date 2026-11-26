from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import Mentor, Booking


# 👨‍🏫 MENTOR DASHBOARD
@login_required
def mentor_dashboard(request):
    mentor = Mentor.objects.filter(user=request.user).first()
    bookings = Booking.objects.filter(mentor__user=request.user).order_by('-id')

    total = bookings.count()
    pending = bookings.filter(status='pending').count()
    accepted = bookings.filter(status='accepted').count()
    rejected = bookings.filter(status='rejected').count()
    cancelled = bookings.filter(status='cancelled').count()

    return render(request, 'mentor_dashboard.html', {
        'mentor': mentor,
        'bookings': bookings,
        'total': total,
        'pending': pending,
        'accepted': accepted,
        'rejected': rejected,
        'cancelled': cancelled
    })


@login_required
def accept_booking(request, id):
    booking = get_object_or_404(Booking, id=id, mentor__user=request.user)
    booking.status = 'accepted'
    booking.save()
    messages.success(request, "Session request accepted.")
    return redirect('/mentor/dashboard/')


@login_required
def reject_booking(request, id):
    booking = get_object_or_404(Booking, id=id, mentor__user=request.user)
    booking.status = 'rejected'
    booking.save()
    messages.info(request, "Session request declined.")
    return redirect('/mentor/dashboard/')


@login_required
def cancel_booking(request, id):
    """Students can cancel their pending booking requests"""
    booking = get_object_or_404(Booking, id=id, student=request.user)
    booking.status = 'cancelled'
    booking.save()
    messages.info(request, "Booking request cancelled.")
    return redirect('/mentor/my-bookings/')


# 👨‍🎓 LIST OF MENTORS (Search by Name, Skill, or Expertise)
@login_required
def mentor_list(request):
    query = request.GET.get('q', '').strip()
    mentors = Mentor.objects.all()

    if query:
        mentors = mentors.filter(
            Q(user__username__icontains=query) |
            Q(skill__icontains=query) |
            Q(expertise__icontains=query)
        )

    return render(request, 'mentor_list.html', {'mentors': mentors})


# 📅 BOOK MENTOR (With Duplicate Slot Validation)
@login_required
def book_mentor(request, mentor_id):
    mentor = get_object_or_404(Mentor, id=mentor_id)

    if request.method == 'POST':
        date = request.POST.get('date')
        time = request.POST.get('time')

        # 🔒 Validation: Prevent duplicate bookings for the same mentor, date, and time
        slot_already_taken = Booking.objects.filter(
            mentor=mentor,
            date=date,
            time=time
        ).exclude(status__in=['rejected', 'cancelled']).exists()

        if slot_already_taken:
            messages.error(request, "This time slot is already booked for this mentor! Please choose a different date or time.")
            return redirect(f'/mentor/book/{mentor_id}/')

        Booking.objects.create(
            student=request.user,
            mentor=mentor,
            date=date,
            time=time,
            status='pending'
        )

        messages.success(request, "Booking request sent successfully!")
        return redirect('/mentor/my-bookings/')

    return render(request, 'book.html', {'mentor': mentor})


# 📄 MY BOOKINGS
@login_required
def my_bookings(request):
    bookings = Booking.objects.filter(student=request.user).order_by('-id')
    return render(request, 'my_bookings.html', {'bookings': bookings})


# 🔄 DYNAMIC AVAILABILITY TOGGLE
@login_required
def toggle_availability(request):
    mentor = Mentor.objects.filter(user=request.user).first()
    if mentor:
        mentor.is_available = not mentor.is_available
        mentor.save()

    return redirect('/mentor/dashboard/')
