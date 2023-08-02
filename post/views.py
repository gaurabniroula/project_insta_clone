from django.shortcuts import render
from post.models import Post
# Create your views here.


def home_feed(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, 'home_feed.html', context)


def add_post(request):
    return render(request, "add_post.html")
