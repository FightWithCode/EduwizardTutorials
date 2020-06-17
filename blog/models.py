from django.db import models
from django.urls import reverse
import random, string


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
	language = models.CharField(max_length=10, default="English")
	is_available_in_hindi = models.BooleanField(default=False)
	post_hash = models.CharField(max_length=10, default=0)

	def __str__(self):
		return self.title

	def save(self, *args, **kwargs):
		if self.slug == "test":
			self.slug = self.title.replace(' ', '-')
			for i in "?.|":
				self.slug = self.slug.replace(i, "").lower()
		if self.post_hash == "test":
			self.post_hash = ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))
		super(Blog, self).save(*args, **kwargs)

	def get_absolute_url(self):
		return reverse('BlogDetailView', kwargs={'slug': self.slug})
