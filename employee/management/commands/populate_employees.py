from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from employee.models import Employee

class Command(BaseCommand):
    help = 'Populate Employee model with dummy data using Faker'

    def add_arguments(self, parser):
        parser.add_argument('total', type=int, help='Indicates the number of employees to be created')

    def handle(self, *args, **kwargs):
        fake = Faker()

        total = kwargs['total']

        for _ in range(total):
            name = fake.name()
            department = fake.job()
            blood_group = fake.random_element(elements=('A+', 'B+', 'O+', 'AB+', 'A-', 'B-', 'O-', 'AB-'))
            dob = fake.date_of_birth(minimum_age=18, maximum_age=65)
            age_years = timezone.now().year - dob.year
            mobile = fake.phone_number()[:14]  # Ensure mobile number does not exceed 14 characters
            gender = fake.random_element(elements=('Male', 'Female'))
            date_joined = timezone.now()  # Use timezone.now() for aware datetime

            # Create Employee instance with dummy data
            employee = Employee(
                username=name.lower().replace(' ', '_'),  # Generate username from name
                name=name,
                department=department,
                blood_group=blood_group,
                dob=dob,
                age_years=age_years,
                mobile=mobile,
                gender=gender,
                date_joined=date_joined
            )

            employee.set_password('Vikas@123')  # Set default password for the employee
            employee.save()

        self.stdout.write(self.style.SUCCESS(f'Successfully populated {total} employees with dummy data'))
