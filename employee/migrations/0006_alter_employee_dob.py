# Generated by Django 5.0.4 on 2024-05-09 09:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0005_alter_employee_is_active_alter_employee_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='dob',
            field=models.DateField(null=True),
        ),
    ]