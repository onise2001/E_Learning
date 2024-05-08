from django.db import models
from django.contrib.auth.models import AbstractUser
#from el_platform.models import Course
# Create your models here.


class User(AbstractUser):
    class Role(models.TextChoices):
        TEACHER = "TEACHER", "Teacher"
        STUDENT = "STUDENT", "Student"

    role = models.CharField(max_length=50, choices=Role.choices, default=Role.TEACHER)
    courses = models.ManyToManyField(to="el_platform.course")
    