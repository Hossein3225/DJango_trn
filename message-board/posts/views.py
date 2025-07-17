from django.shortcuts import render

# Create your views here.
from .models import post
from django.views.generic import ListView

# this django generic is the way to create a list view
# def post_view(request):
#    posts = post.objects.all()
#    return render(request, "post_list.html", {"posts": posts})


class post_view(ListView):
    template_name = "post_list.html"
    model = post
    # this class creat a list that name is "modelname_list"
