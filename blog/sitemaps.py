from django.contrib.sitemaps import Sitemap
from .models import Blog


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.9
 
    def items(self):
        return Blog.objects.filter(public=True)
 
    def lastmod(self, obj):
    	return obj.date
