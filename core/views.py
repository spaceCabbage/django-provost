from .models import Post, Comment
from django.shortcuts import render, get_object_or_404
import json
from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    qs = Post.objects.all()
    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, status=200, safe=False)


def post_list(request):
    posts = Post.objects.all()
    post_list = []

    for post in posts:
        comments = Comment.objects.filter(post=post)
        comment_list = [
            {
                "content": comment.content,
                "created_at": comment.created_at,
                "user": comment.user.username,
            }
            for comment in comments
        ]
        post_data = {
            "id": post.id,
            "title": post.title,
            "content": post.content,
            "created_at": post.created_at,
            "user": post.user.username,
            "comments": comment_list,
        }
        post_list.append(post_data)

    context = {"posts": post_list}
    return render(request, "core/post_list.html", context)


def post_detail(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    comments = Comment.objects.filter(post=post)
    comment_list = [
        {
            "content": comment.content,
            "created_at": comment.created_at,
            "user": comment.user.username,
        }
        for comment in comments
    ]

    context = {
        "post": post,
        "comments": comment_list,
    }
    return render(request, "core/post_detail.html", context)
