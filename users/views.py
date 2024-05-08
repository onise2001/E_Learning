from django.shortcuts import render, redirect
from .forms import RegistrationForm, LoginForm
from .models import User
from django.contrib.auth.models import Group 
from django.contrib.auth import authenticate, login, logout
# Create your views here.


def signup(request):

    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = User.objects.create_user(first_name=data["first_name"],last_name=data["last_name"],username=data["username"],password=data["password"],role=data["role"])
            #print(user)
            if user.role == "STUDENT":
               user.groups.add(1)
            else: 
               user.groups.add(2)
            return redirect("/")
        return redirect("signup")

    form = RegistrationForm
    return render(request, "users/signup.html", {"form": form})




def signin(request):

    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data["username"], password=data["password"])
            if user is not None:
                login(request, user)
                return redirect("/")
            return redirect("login")

    form = LoginForm
    return render(request, "users/login.html", {"form": form})


def logout_user(request):
    logout(request)
    return redirect("/")