from django.shortcuts import render
from .models import Hello
# Create your views here.
# GET hello/
def hello(request):
    
    # ORM => Object Relation Mapping
    # Python Code <=> SQL
    # SELECT * 
    post = Hello.objects.all()

    context = {
        'post': post
    }
    return render(request, 'hello/index.html', context=context)