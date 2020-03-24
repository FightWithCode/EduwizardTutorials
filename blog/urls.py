from django.conf.urls import url
from django.urls import path
from . import views


urlpatterns = [
    # url(r'^blog/(?P<slug>[-\w]+)/$', views.BlogDetailView, name="BlogDetailView"),
    path('blog/<str:slug>/', views.BlogDetailView, name='BlogDetailView'),
]

