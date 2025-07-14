from django.urls import path
from .views import home_page_view
from .views import abot_pages_view

urlpatterns = [
    path("about/", abot_pages_view),
    path("", home_page_view),
]
