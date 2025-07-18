from django.shortcuts import render, get_object_or_404

# Create your views here.
from .models import post


def Post_List(request):
    posts = post.objects.all()
    return render(request, "home.html", {"posts": posts})


def post_detail(request, pk):
    Post = get_object_or_404(post, pk=pk)
    return render(request, "post_detail.html", {"Post": Post})
