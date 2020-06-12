from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    path('class/<str:std>/<str:subject>', views.ClassNotesView, name="ClassNotesView"),
    url(r'^class/(?P<std>[\w]+)/available_subjects/$', views.ClassNotesAllSubjectView, name="ClassNotesAllSubjectView"),
    url(r'^download/(?P<slug>[\w/.-]+)/$', views.NotesDownloadView, name="NotesDownloadView"),
]
