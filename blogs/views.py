from django.shortcuts import render
from .models import Blog
from django.http import HttpResponse


def posts_by_category(request,category_id):
    posts= Blog.objects.filter(status='Published', category_id=category_id)
    context = { 'posts': posts}
    return render(request, 'posts_by_category.html', context)
