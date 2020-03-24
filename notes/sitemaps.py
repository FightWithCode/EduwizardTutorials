from django.contrib import sitemaps
from .models import Note


class NoteSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Note.objects.all()
 
    def lastmod(self, obj):
    	return obj.date
