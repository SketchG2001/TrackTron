# Generated by Django 5.0.4 on 2024-05-09 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0007_alter_employee_age_years'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='is_active',
            field=models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active'),
        ),
        migrations.AlterField(
            model_name='employee',
            name='is_staff',
            field=models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status'),
        ),
    ]