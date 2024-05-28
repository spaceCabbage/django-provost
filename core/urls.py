from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # Home
    path("", views.home, name="home"),
    # Posts
    path("posts/", views.post_list, name="post_list"),
    path("posts/raw", views.post_list_raw, name="post_list_raw"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("admin/", admin.site.urls),
]
