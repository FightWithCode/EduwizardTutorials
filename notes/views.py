from django.shortcuts import render, redirect
from .models import Note
from django.shortcuts import get_object_or_404
from .forms import NotesQueryForm


available_subject_of_classes = {
	'6': ['Science'],
	'7': ['Science'],
	'8': ['Science'],
	'9': ['Science', 'English', 'History', 'Geography', 'Political Science'],
	'10': ['Science', 'English', 'History', 'Geography', 'Political Science', 'Economics', 'Math Sample Papers', 'Science Sample Papers'],
	'11': ['English', 'Biology', 'Chemistry', 'Physics', 'Pol Science', 'History', 'Computer Science'],
	'12': ['English', 'Biology', 'Chemistry', 'Physics', 'Pol Science', 'History', 'Computer Science', 'Math Sample Papers'],
}


def ClassNotesView(request, std, subject):
	objs = Note.objects.filter(note_class__iexact=std, subject__iexact=subject).order_by('chapter_no')

	form = NotesQueryForm()

	if request.method == 'POST':
		form = NotesQueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'notes/class_notes.html', {'notes': objs, 'note_class': std, 'form': form, 'note_subject': subject})


def ClassNotesAllSubjectView(request, std):
	note_class = std
	available_subjects = available_subject_of_classes.get(note_class)

	form = NotesQueryForm()

	if request.method == 'POST':
		form = NotesQueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'notes/available_subjects.html', {'note_class': note_class, 'form': form, 'available_subjects': available_subjects})


def NotesDownloadView(request, slug):
	obj = get_object_or_404(Note, slug__iexact=slug)
	notes_obj = Note.objects.filter(note_class__iexact=obj.note_class)[:5]
	pdfurl = obj.notes_document
	if obj.is_paid:
		pdfurl = obj.preview_document
	return render(request, 'notes/class_notes_download.html', {'pdfurl': pdfurl, 'obj': obj, 'notes_obj': notes_obj})


