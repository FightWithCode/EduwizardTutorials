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
	tags = models.CharField(max_length=200)
	public = models.BooleanField()
	meta_description = models.CharField(max_length=200)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug == "":
			self.slug = self.title.replace(' ', '-')
			for i in "?.":
				self.slug = self.slug.replace(i, "").lower()
		super(Blog, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('BlogDetailView', kwargs={'slug': self.slug})
