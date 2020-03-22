from django.shortcuts import render
from .models import Note
from django.shortcuts import get_object_or_404


def ClassNotesView(request, std):
	objs = Note.objects.filter(note_class__iexact=std)
	print(objs)
	return render(request, 'notes/class_notes.html', {'notes': objs})


def NotesDownloadView(request, pdfurl):
	obj = get_object_or_404(Note, notes_document__iexact=pdfurl)
	notes_obj = Note.objects.filter(note_class__iexact=obj.note_class)[:5]
	return render(request, 'notes/class_notes_download.html', {'pdfurl': pdfurl, 'obj': obj, 'notes_obj': notes_obj})
