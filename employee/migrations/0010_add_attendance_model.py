# Generated by Django 5.0.4 on 2024-05-11 08:31

import django.db.models.deletion
import django.utils.timezone
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0009_leaverequest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attendance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('time', models.TimeField(default=django.utils.timezone.now)),
                ('location', models.CharField(max_length=255)),
                ('status', models.CharField(choices=[('present', 'Present'), ('absent', 'Absent'), ('late', 'Late')], max_length=20)),
                ('comments', models.TextField(blank=True)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
