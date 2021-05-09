from django.shortcuts import render
from .forms import JoinQueryForm
from django.shortcuts import redirect
from blog.models import Blog
from .models import NewsLetter
import os
from django.conf import settings
from django.http import HttpResponse
from notes.models import Note
from notes.forms import NotesQueryForm


def IndexView(request):
	objs = Blog.objects.filter(public=True).order_by('-id')[:4]
	first_obj = objs.first()
	objs = objs[1:4]
	print(objs)
	print(first_obj.front_image_500)
	return render(request, 'index.html', {'objs': objs, 'first_obj': first_obj})


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


def PrivacyView(request):
	return render(request, 'privacy.html', {})


def TeachersView(request):
	return render(request, 'teachers.html', {})


def GalleryView(request):
	return render(request, 'gallery.html', {})


def CoursesView(request):
	return render(request, 'courses.html', {})


def NotesView(request):
	return render(request, 'notes.html', {})


def BlogView(request):
	obj = Blog.objects.filter(public=True).order_by('-id')
	return render(request, 'blog.html', {'blogs': obj})


def SubmitThankView(request):
	return render(request, 'submit_thankyou.html', {})


def sw_js(request):
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/sw.js")
    print(full_script_path)
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text/javascript")


def AdsTxtView(request):
    full_script_path = os.path.join(settings.STATIC_ROOT, "js/ads.txt")
    with open(full_script_path, 'r') as f:
        javascript_contents = f.read()
    return HttpResponse(javascript_contents, content_type="text")


def NewsLetterView(request):
	email = request.POST.get('email')
	if ('@' and '.') in email:
		NewsLetter.objects.create(email=email)
		return HttpResponse("<center>Thanks for Subscribing our New Letter<br><a href=\"https://www.eduwizardtutorials.com\">Home</a></center>")
	else:
		return HttpResponse("<center>Not a Valid Email<br><a href=\"https://www.eduwizardtutorials.com\">Home</a></center>")


def SearchNotesView(request):
	search_class = request.GET.get("class")
	search_subject = request.GET.get("subject")
	if search_class and search_subject:
		objs = Note.objects.filter(note_class__iexact=search_class, subject__iexact=search_subject).order_by('chapter_no')
	elif search_class and (search_subject is "" or search_subject is None):
		objs = Note.objects.filter(note_class__iexact=search_class).order_by('chapter_no')
	elif search_subject and (search_class is "" or search_class is None):
		objs = Note.objects.filter(subject__iexact=search_subject).order_by('chapter_no')

	form = NotesQueryForm()
	if request.method == 'POST':
		form = NotesQueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'search_notes.html', {"objs": objs, 'form': form})
