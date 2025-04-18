from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm

# Create your views here.


def test_view(request):
    return HttpResponse(f"Hello, world {random.randint(1, 100)}!")

def home_html_view(request):
    return render(request, "base.html")


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post/post_list.html", {"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/post_detail.html", {"post": post})


def create_post_view(request):
    if request.method == "GET":
        form = PostForm()
        return render(request, "post/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "post/post_create.html", context={"form": form})
        elif form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect("/posts/create/")

