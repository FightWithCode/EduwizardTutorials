from django.urls import re_path as url
from django.urls import path
from . import views


urlpatterns = [
    path('class/<str:std>/<str:subject>/notes', views.ClassNotesView, name="ClassNotesView"),
    url(r'^class/(?P<std>[\w]+)/available_subjects/$', views.ClassNotesAllSubjectView, name="ClassNotesAllSubjectView"),
    # url(r'^download/(?P<slug>[\w/.-]+)/$', views.NotesDownloadView, name="NotesDownloadView"),
    path('download/<str:slug>/', views.NotesDownloadView, name='NotesDownloadView'),
]
