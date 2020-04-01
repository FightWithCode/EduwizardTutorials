from django.shortcuts import render, redirect
from .models import Note
from django.shortcuts import get_object_or_404
from. forms import NotesQueryForm


def ClassNotesView(request, std):
	objs = Note.objects.filter(note_class__iexact=std).order_by('chapter_no')
	note_class = std
	note_subject = "Science"

	form = NotesQueryForm()

	if request.method == 'POST':
		form = NotesQueryForm(request.POST)
		if form.is_valid():
			form.save(commit=True)
			return redirect('SubmitThankView')
		else:
			print("Form Invalid")
	return render(request, 'notes/class_notes.html', {'notes': objs, 'note_class': note_class, 'form': form, 'note_subject': note_subject})


def NotesDownloadView(request, pdfurl):
	obj = get_object_or_404(Note, notes_document__iexact=pdfurl)
	notes_obj = Note.objects.filter(note_class__iexact=obj.note_class)[:5]
	return render(request, 'notes/class_notes_download.html', {'pdfurl': pdfurl, 'obj': obj, 'notes_obj': notes_obj})
