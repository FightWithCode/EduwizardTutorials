from django.shortcuts import render
from .models import Blog
from django.shortcuts import get_object_or_404


def BlogDetailView(request, slug):
	obj = get_object_or_404(Blog, slug__iexact=slug)
	print(obj.title)
	return render(request, "blogs/blog_detail.html", {'blog': obj})
