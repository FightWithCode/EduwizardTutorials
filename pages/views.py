from django.shortcuts import render
from .forms import JoinQueryForm
from django.shortcuts import redirect
from blog.models import Blog


def IndexView(request):
	return render(request, 'index.html', {})


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
	obj = Blog.objects.filter(public=True).order_by('-date')[:10]
	return render(request, 'blog.html', {'blogs': obj})


def SubmitThankView(request):
	return render(request, 'submit_thankyou.html', {})


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


# def JoinQueryView(request):
