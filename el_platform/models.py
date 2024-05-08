from django.db import models
from users.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name




class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #users = models.ManyToManyField(to='users.User', related_name="mycourses", blank=True)


class Stage(models.Model):
    title = models.CharField(max_length=100)
    video = models.URLField()
    text = models.TextField()
    course = models.ForeignKey(Course, on_delete=models.CASCADE)


class Status(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    finished = models.BooleanField(default=False)
    


