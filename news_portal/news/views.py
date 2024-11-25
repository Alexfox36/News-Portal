from django.shortcuts import render

# Create your views here.

from django.views.generic import TemplateView, ListView
from .models import Post

class BaseView(TemplateView):
    template_name = 'base.html'

class PostsList(ListView):
    model = Post
    ordering = 'post_date_time'
    template_name = 'posts.html'
    context_object_name = 'posts_list'