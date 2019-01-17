from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContentForm
from .models import Content
# Create your views here.

def content_list(request):
    contents = Content.objects.all()
    return render(request, 'crud_fbv/content_list.html', {'contents':contents})

def content_view(request, pk):
    content = get_object_or_404(Content, pk=pk)
    return render(request, 'crud_fbv/content_detail.html', {'content':content})

def content_create(request):
    form = ContentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('content_list')
    return render(request, 'crud_fbv/content_form.html', {'form':form})

def content_update(request, pk):
    content = get_object_or_404(Content, pk=pk)
    form = ContentForm(request.POST or None, instance=content)
    if form.is_valid():
        form.save()
        return redirect('content_list')
    return render(request, 'crud_fbv/content_form.html', {'form':form})

def content_delete(request, pk):
    content = get_object_or_404(Content, pk=pk)
    if request.method=='POST':
        content.delete()
        return redirect('content_list')
    return render(request, 'crud_fbv/content_confirm_delete.html', {'object':content})