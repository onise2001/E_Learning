# Generated by Django 5.0.4 on 2024-05-06 21:10

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('el_platform', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='users',
            field=models.ManyToManyField(related_name='mycourses', to=settings.AUTH_USER_MODEL),
        ),
    ]