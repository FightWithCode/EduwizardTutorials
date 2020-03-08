from django.db import models


class Note(models.Model):
    note_class = models.CharField(max_length=10)
    subject = models.CharField(max_length=25)
    chapter = models.CharField(max_length=25)
    notes_document = models.FileField(upload_to='documents/')
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
