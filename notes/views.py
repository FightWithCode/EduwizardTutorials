from django.shortcuts import render
from .models import Note


def ClassNotesView(request, std):
	objs = Note.objects.filter(note_class__iexact=std)
	return render(request, 'notes/class_notes.html', {'notes': objs})
