from django.db import models
from django.contrib.auth.hashers import make_password
from datetime import datetime


class Employee(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    department = models.CharField(max_length=100, null=False, blank=False)
    blood_group = models.CharField(max_length=5, null=False, blank=False)
    dob = models.DateField(null=False, blank=False)
    age_years = models.IntegerField(null=False, blank=False)
    email = models.EmailField(unique=True, null=False, blank=False)  # Unique email address, not nullable
    mobile = models.CharField(max_length=14, unique=True, null=False, blank=False)  # Unique mobile number, not nullable
    password = models.CharField(max_length=100, null=False, blank=False)
    gender = models.CharField(max_length=10, null=False, blank=False)

    def save(self, *args, **kwargs):
        # Convert the dob to a datetime object if it's a string
        if isinstance(self.dob, str):
            self.dob = datetime.strptime(self.dob, '%d-%m-%y').date()

        # Hash the password before saving
        if self.password and not self.password.startswith('pbkdf2_sha256$'):
            self.password = make_password(self.password)

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
