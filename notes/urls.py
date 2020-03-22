from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^class/(?P<std>[\w]+)/$', views.ClassNotesView, name="ClassNotesView"),
    url(r'^download/(?P<pdfurl>[\w/.-]+)/$', views.NotesDownloadView, name="NotesDownloadView"),
]
