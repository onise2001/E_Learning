from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
# Create your views here.

def forum(request):
    posts = Post.objects.all()
    return render(request, "forum/forum.html", {"posts": posts})

def see_post(request, id):
    post = Post.objects.get(pk=id)
    comments = Comment.objects.filter(post=post)
    comment_form = CommentForm
    return render(request, "forum/see_post.html", {"post": post, "comments": comments, "comment_form":comment_form})
    

def add_post(request):
    if request.user.is_authenticated:

        if request.method == "POST":
            form = PostForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.create(title=data['title'], text=data['text'], user=request.user)
                return redirect("forum") 
    
        form = PostForm
        return render(request, "forum/add_post.html", {"form": form})

# def edit_post(request, id):
#     post = Post.objects.filter(pk=id)[0]
#     if request.mehtod == "POST":
#         form = PostForm(request.POST, instance=post)
#         if form.is_valid():
#             form.save()
#     form = PostForm(instance=post)
#     return render(request, "forum/edit_post.html", {"form": form})



def delete_post(request, id):
    if request.user.has_perm("forum.delete_post"):
        post = Post.objects.get(pk=id).delete()
        return redirect("forum")

def add_comment(request, id):
    if request.user.is_authenticated:
        if request.method == "POST":
            form = CommentForm(request.POST)
            if form.is_valid():
                data = form.cleaned_data
                post = Post.objects.get(pk=id)
                comment = Comment.objects.create(user=request.user, post=post, text=data['text'] )
                print(comment)
                comment.save()
            
            return redirect("post", id=id)

def delete_comment(request, id):
    comment = Comment.objects.get(pk=id)
    post = comment.post
    comment.delete()
    return redirect("post", id=post.id)

# def edit_comment(request, id):
#     ...