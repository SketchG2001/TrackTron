from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

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




