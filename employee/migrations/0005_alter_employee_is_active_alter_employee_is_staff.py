# Generated by Django 5.0.4 on 2024-05-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0004_alter_employee_date_joined'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=True),
        ),
    ]
