from .models import Post
import json
from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    qs = Post.objects.all()
    serialized_data = serialize("json", qs)
    serialized_data = json.loads(serialized_data)
    return JsonResponse(serialized_data, status=200, safe=False)
