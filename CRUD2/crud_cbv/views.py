from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Content

class ContentList(ListView):
    model = Content

class ContentView(DetailView):
    model = Content

class ContentCreate(CreateView):
    model = Content
    fields = ['title', 'text']
    success_url = reverse_lazy('content_list')

class ContentUpdate(UpdateView):
    model = Content
    fields = ['title', 'text']
    success_url = reverse_lazy('content_list')

class ContentDelete(DeleteView):
    model = Content
    success_url = reverse_lazy('content_list')