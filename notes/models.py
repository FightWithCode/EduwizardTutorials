from django.db import models
from django.urls import reverse


class Note(models.Model):
    note_class = models.CharField(max_length=10)
    subject = models.CharField(max_length=25)
    chapter_no = models.CharField(max_length=2)
    chapter_name = models.CharField(max_length=50)
    notes_document = models.FileField(upload_to='documents/')
    language = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
    	return self.note_class + ' | ' + self.subject + ' | ' + self.chapter_name + ' | ' + self.language

    def get_absolute_url(self):
        return reverse('notes:NotesDownloadView', kwargs={'pdfurl': self.notes_document})
