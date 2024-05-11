from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime
from django.utils import timezone
class Employee(AbstractUser):
    name = models.CharField(max_length=30, null=False, blank=False)
    department = models.CharField(max_length=100, null=False, blank=False)
    blood_group = models.CharField(max_length=5, null=False, blank=False)
    dob = models.DateField(null=True, blank=False)
    age_years = models.IntegerField(null=True, blank=False)
    mobile = models.CharField(max_length=14, unique=True, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)
    date_joined = models.DateTimeField(null=True, blank=True)

    # is_staff = models.BooleanField(default=True)  # Set default value for is_staff
    # is_active = models.BooleanField(default=True)  # Set default value for is_active

    def __str__(self):
        return self.username

    def save(self, *args, **kwargs):
        # self.is_staff = True  # Set is_staff to True
        # self.is_active = True  # Set is_active to True

        # Convert the dob to a datetime object if it's a string
        if isinstance(self.dob, str):
            self.dob = datetime.strptime(self.dob, '%d-%m-%y').date()

        super().save(*args, **kwargs)

class LeaveRequest(models.Model):
    LEAVE_TYPES = [
        ('annual', 'Annual Leave'),
        ('sick', 'Sick Leave'),
        ('personal', 'Personal Leave'),
        # Add more leave types as needed
    ]

    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    leave_type = models.CharField(max_length=20, choices=LEAVE_TYPES)
    start_date = models.DateField()
    end_date = models.DateField()
    reason = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=20, default='pending')  # 'pending', 'approved', 'rejected'

    def __str__(self):
        return f"{self.employee.name} - {self.get_leave_type_display()}"


class Attendance(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=255)
    STATUS_CHOICES = [
        ('present', 'Present'),
        ('absent', 'Absent'),
        ('late', 'Late'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    comments = models.TextField(blank=True)

    def __str__(self):
        return f"{self.employee.username} - {self.date} - {self.time}"

    class Meta:
        verbose_name_plural = "Attendance"
        unique_together = ('employee', 'date')
