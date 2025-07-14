from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def home_page_view(request):
    return HttpResponse("Homepage")


def abot_pages_view(request):
    context = {
        "name": "Jafar",
        "age": 50,
        "job": "artist",
    }
    return render(request, "pages/about.html", context)
