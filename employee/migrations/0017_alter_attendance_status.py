# Generated by Django 5.0.4 on 2024-05-13 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0016_attendance_on_leave'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='status',
            field=models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'late')], max_length=20),
        ),
    ]
