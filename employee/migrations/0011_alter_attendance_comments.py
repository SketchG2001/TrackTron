# Generated by Django 5.0.4 on 2024-05-11 09:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0010_add_attendance_model'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='comments',
            field=models.TextField(blank=True, null=True),
        ),
    ]
