from django.urls import path
from .views import Post_List, post_detail

urlpatterns = [
    path("", Post_List, name="home"),
    path("post/<int:pk>/", post_detail, name="post_detail"),
]
