from django.db import models
from django.contrib.auth.models import User

class Mentor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    expertise = models.CharField(max_length=200)
    experience = models.IntegerField()
    skill=models.CharField(max_length=100)
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return self.user.username

class Booking(models.Model):
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(null=True, blank=True)
    time = models.TimeField(null=True, blank=True)
    
    status = models.CharField(max_length=20, default='pending')

    class Meta:
        unique_together = ['student', 'mentor', 'date', 'time']  # 🔥 updated

def __str__(self):
    return f"{self.student.username} booked {self.mentor.user.username}"

# Create your models here.
