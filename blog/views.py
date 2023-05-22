from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import *

# Create your views here.

def index(request):
    all_post = Post.objects.filter(published = True)
    category = Category.objects.filter(published = True)

    context = {
        'all_post' : all_post,
        'category': category,
    }
    return render(request, 'index.html', context)
