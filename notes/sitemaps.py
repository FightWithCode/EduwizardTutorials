from django.contrib import sitemaps
from .models import Note, Classes


class NoteSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Note.objects.all().order_by('-date')
 
    def lastmod(self, obj):
    	return obj.date


class NoteClassSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'monthly'

    def items(self):
        return Classes.objects.all().order_by('-date')
 
    def lastmod(self, obj):
    	return obj.date
