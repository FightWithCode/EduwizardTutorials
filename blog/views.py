from django.shortcuts import render
from .models import Blog


def BlogDetailView(request, slug):
	obj = Blog.objects.filter(slug__iexact=slug)
	return render(request, "blogs/blog_detail.html", {'blog_obj': obj})
