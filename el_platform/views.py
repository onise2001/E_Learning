from django.shortcuts import render, redirect
from .models import Course,Category, Stage, Status
from .forms import AddCourseForm, AddStageForm

# Create your views here.

def index(request):
    courses = Course.objects.all()
    categories = Category.objects.all()
    return render(request, "el_platform/show_all.html" ,{"items": courses, "categories": categories})



def my_courses(request):
    if request.user.is_authenticated:
       my_courses = request.user.courses.filter(user=request.user)
       return render(request, "el_platform/my_courses.html", {"courses": my_courses})
    return redirect("/auth/login")


def create_course(request):
    if request.user.is_authenticated:
        if request.user.has_perm("el_platform.add_course"):
            if request.method == "POST":
                form = AddCourseForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    course = Course.objects.create(name=data["name"], description=data["description"], category=data["category"])
                    status = Status(user=request.user, course=course)
                    status.save()
                    course.save()
    
                    request.user.courses.add(course.id)
                    
                    
        form = AddCourseForm
        return render(request, "el_platform/create_course.html", {"form": form})
    return redirect("/auth/login")


def delete_course(request,id):
    if request.user.is_authenticated:
        if request.user.has_perm("el_platform.delete_course"):
            course = Course.objects.filter(pk=id)
            if course is not None:
                course.delete()
                return redirect("/")
    return redirect("/auth/login")


def see_course(request,id):
    course = Course.objects.filter(pk=id)
    stages = Stage.objects.filter(course=course[0])
    #print(course.values())
    if request.user.is_authenticated:
        joined = request.user.courses.filter(user=request.user, id=course[0].id)
        #print(joined)
        if len(joined) != 0:
            finished = Status.objects.filter(user=request.user.id, course=course[0])
            return render(request, "el_platform/course.html", {"course": course[0], "stages": stages, "joined": True, "finished":finished[0].finished})

    
    return render(request, "el_platform/course.html", {"course": course[0], "stages": stages})


def edit_course(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm("el_platform.change_course"):
            course = Course.objects.filter(pk=id)[0]
            if request.method == "POST":
                form = AddCourseForm(request.POST)
                if form.is_valid():
                    data = form.cleaned_data
                    course.name = data["name"]
                    course.description = data["description"]
                    course.category = data["category"]
                    course.save()
                    return redirect("mycourses")
            
            form = AddCourseForm(instance=course)
            return render(request, "el_platform/edit_course.html", {"form": form})
    return redirect("/auth/login")




def add_stage(request, id):
    if request.user.is_authenticated:

        if request.user.has_perm("el_platform.add_stage"):
            if request.method == "POST":
                form = AddStageForm(request.POST)
                if form.is_valid():
                    course = Course.objects.filter(pk=id)
                    data = form.cleaned_data
                    stage = Stage.objects.create(title=data['title'], video=data['video'], text=data['text'], course=course[0])
                    #stage.course = course
    
    
            form = AddStageForm
            return render(request, "el_platform/add_stage.html", {"form": form})
    return redirect("/auth/login")
    


def del_stage(request, id):
    if request.user.is_authenticated:
        if request.user.has_perm("el_platform.delete_stage"):
            Stage.objects.filter(pk=id).delete()
            return redirect("home")
    return redirect("/auth/login")


def join_course(request, id):
    if request.user.is_authenticated:
        course = Course.objects.get(pk=id)
        request.user.courses.add(course.id)
        status = Status(user=request.user,course=course)
        status.save()
        return redirect("mycourses")
    return redirect("/auth/login")
    
def finish_course(request, id):
    if request.user.is_authenticated:
        #course = request.users.courses.filter(user=request.user.id, course=id)
        status = Status.objects.filter(user=request.user.id, course=id)[0]
        status.finished = True
        status.save()
        return redirect("mycourses") 
    return redirect("/auth/login")


