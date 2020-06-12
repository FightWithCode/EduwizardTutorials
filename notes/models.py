from django.db import models
from django.urls import reverse


class Note(models.Model):
    note_class = models.CharField(max_length=10)
    subject = models.CharField(max_length=25)
    chapter_no = models.IntegerField()
    chapter_name = models.CharField(max_length=50)
    notes_document = models.FileField(upload_to='documents/')
    language = models.CharField(max_length=25)
    description = models.CharField(max_length=255, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    date = models.DateTimeField(auto_now_add=True)
    slug = models.CharField(max_length=100)

    def save(self, *args, **kwargs):
        slug_to_be_saved = 'class' + '-' + self.note_class + '-' + self.subject + '-chapter-' + str(self.chapter_no) + '-' + self.chapter_name + '-' + 'notes'
        self.slug = slug_to_be_saved.replace(' ', '-').lower()
        super(Note, self).save(*args, **kwargs)

    def __str__(self):
    	return self.note_class + ' | ' + self.subject + ' | ' + self.chapter_name + ' | ' + self.language

    def get_absolute_url(self):
        return reverse('NotesDownloadView', kwargs={'slug': self.slug})


class Classes(models.Model):
    standard = models.CharField(max_length=10)
    subject = models.CharField(max_length=25)
    date = models.TimeField(auto_now=True)

    def __str__(self):
        return self.standard + ' | ' + self.subject

    def get_absolute_url(self):
        return reverse('ClassNotesView', kwargs={'std': self.standard, 'subject': self.subject})
