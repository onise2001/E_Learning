# Generated by Django 5.0.4 on 2024-05-06 22:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('el_platform', '0002_course_users'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='course',
            name='users',
        ),
    ]
