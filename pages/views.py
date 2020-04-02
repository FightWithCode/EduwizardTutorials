from django.shortcuts import render
from .forms import JoinQueryForm
from django.shortcuts import redirect
from blog.models import Blog
import os
from django.conf import settings
from django.http import HttpResponse


def IndexView(request):
	return render(request, 'index.html', {})


def ContactView(request):
	form = JoinQueryForm()

	if request.method == 'POST':
		form = JoinQueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'contact.html', {'form': form})


def AboutView(request):
	return render(request, 'about.html', {})


def TeachersView(request):
	return render(request, 'teachers.html', {})


def GalleryView(request):
	return render(request, 'gallery.html', {})


def CoursesView(request):
	return render(request, 'courses.html', {})


def NotesView(request):
	return render(request, 'notes.html', {})


def BlogView(request):
	obj = Blog.objects.filter(public=True).order_by('-id')[:10]
	return render(request, 'blog.html', {'blogs': obj})


def SubmitThankView(request):
	return render(request, 'submit_thankyou.html', {})


def sw_js(request):
    print(settings.STATIC_ROOT)
    print(os.path.join(settings.STATIC_ROOT, "rahul"))
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/sw.js")
    print(full_script_path)
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text/javascript")
