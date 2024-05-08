from django.urls import path
from .views import index, my_courses, create_course, delete_course, see_course, edit_course, add_stage, del_stage, join_course, finish_course

urlpatterns = [
   path("", index, name='home'),
   path("mycourses/",my_courses, name="mycourses" ),
   path("create_course/", create_course, name="createcourse"),
   path("delete_course/<int:id>", delete_course, name="delete"),
   path('course/<int:id>', see_course, name="show"),
   path("edit_course/<int:id>", edit_course, name="edit"),
   path("add_stage/<int:id>", add_stage, name="addstage" ),
   path("delete_stage/<int:id>", del_stage, name="deletestage"),
   path("join_course/<int:id>", join_course, name="join"),
   path("finish_course/<int:id>", finish_course, name="finish" ),
  
]
