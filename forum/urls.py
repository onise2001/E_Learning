from django.urls import path
from .views import forum, add_post, delete_post, see_post, add_comment, delete_comment

urlpatterns = [
    path("", forum, name="forum" ),
    path("see_post/<int:id>", see_post, name="post"),
    path("add_post/", add_post, name="addpost"),
    path("delete_post/<int:id>", delete_post, name="deletepost"),
    #path("edit_post/<int:id>", edit_post, name="editpost"),
    path("add_comment/<int:id>", add_comment, name="addcomment"),
    path("delete_comment/<int:id>", delete_comment, name="deletecomment"),
   
]
