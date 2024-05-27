from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("posts/", views.post_list, name="post_list"),
    path("posts/<int:post_id>/", views.post_detail, name="post_detail"),
    path("admin/", admin.site.urls),
]
