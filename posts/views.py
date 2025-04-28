from django.shortcuts import render, HttpResponse, redirect
import random
from posts.models import Post
from posts.forms import PostForm, PostForm2, SearchForm
from django.contrib.auth.decorators import login_required

# Create your views here.


def test_view(request):
    return HttpResponse(f"Hello, world {random.randint(1, 100)}!")

def home_html_view(request):
    return render(request, "base.html")

@login_required(login_url="/login/")
def post_list_view(request):
    limit = 3
    if request.method == "GET":
        posts = Post.objects.all()
        form = SearchForm()
        search_q = request.GET.get("search_q")
        category_id = request.GET.get("category_id")
        ordering = request.GET.get("ordering")
        page = int(request.GET.get("page", 1))
        if ordering:
            posts = posts.order_by(ordering)
        if category_id:
            posts = posts.filter(category_id=category_id)
        if search_q:
            posts = posts.filter(title__icontains=search_q)

        max_pages = posts.count() / limit + 1
        if round(max_pages) < max_pages:
            max_pages = round(max_pages) + 1
        else: 
            max_pages = round(max_pages)
        start = (page-1) * limit
        end = page * limit
        posts = posts[start:end]
        return render(
            request,
            "post/post_list.html", 
            context={
                "posts": posts, 
                "form": form,
                "max_pages": range(1, int(max_pages) + 1),
                }
            )

@login_required(login_url="/login/")
def post_detail_view(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, "post/post_detail.html", {"post": post})

@login_required(login_url="/login/")
def create_post_view(request):
    if request.method == "GET":
        form = PostForm2()
        return render(request, "post/post_create.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES)
        if not form.is_valid():
            return render(request, "post/post_create.html", context={"form": form})
        elif form.is_valid():
            tags = form.cleaned_data.pop("tags")
            post = Post.objects.create(**form.cleaned_data)
            post.tags.set(tags)
            return redirect("/posts/")


@login_required(login_url='/login')
def post_update_view(request, post_id):
    post = Post.objects.filter(id=post_id, author=request.user).first()
    if not post:
        return HttpResponse("404 Not Found", status=404)
    if request.method == "GET":
        form = PostForm2(instance=post)
        return render(request, "post/post_update.html", context={"form": form})
    if request.method == "POST":
        form = PostForm2(request.POST, request.FILES, instance=post)
        if not form.is_valid():
            return render(request, "post/post_update.html", context={"form": form})
        elif form.is_valid():
            tags = form.cleaned_data.pop("tags")
            form.save()
            post.tags.set(tags)
            return redirect(f"/posts/{post_id}")

@login_required(login_url='/login')
def post_delete_view(request, post_id):
    Post.objects.filter(id=post_id).first().delete()
    return redirect("/profile/")