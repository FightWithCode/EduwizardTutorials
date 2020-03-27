from django.db import models
from django.urls import reverse


class Blog(models.Model):
	title = models.CharField(max_length=100)
	date = models.DateField(auto_now=True)
	front_image = models.CharField(max_length=100)
	slug = models.CharField(max_length=120, default="test")
	description = models.CharField(max_length=500)
	content = models.TextField()
	author = models.CharField(max_length=25)
	public = models.BooleanField()

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		self.slug = self.title.replace(' ', '-')
		super(Blog, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('BlogDetailView', kwargs={'slug': self.slug})
