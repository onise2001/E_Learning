from django.urls import path
from .views import signin, signup, logout_user
urlpatterns = [
    path("login/", signin, name="login"),
    path("signup/", signup, name="signup"),
    path("logout/", logout_user, name="logout"),
]
