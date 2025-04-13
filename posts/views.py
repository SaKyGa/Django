from django.shortcuts import render, HttpResponse
import random
from posts.models import Post

# Create your views here.


def test_view(request):
    return HttpResponse(f"Hello, world {random.randint(1, 100)}!")

def html_view(request):
    return render(request, "base.html")


def post_list_view(request):
    posts = Post.objects.all()
    return render(request, "post/post_list.html", {"posts": posts})


def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/post_detail.html", {"post": post})

