from .views import Homepage, AboutPageView
from django.urls import path

urlpatterns = [
    path("", Homepage, name="home"),
    path("about/", AboutPageView.as_view(), name="about"),
]
