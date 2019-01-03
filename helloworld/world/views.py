from django.shortcuts import render
from .models import World

# Create your views here.
# GET hello/
def world(request):
    
    post = World.objects.all()
    context = {
        'post': post
    }
    return render(request, 'world/index.html', context=context)