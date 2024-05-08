from django import forms
from .models import Course, Stage

class AddCourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ("name", "description", "category",)


class AddStageForm(forms.ModelForm):
    class Meta:
        model = Stage
        fields = ("title", "video", "text",)