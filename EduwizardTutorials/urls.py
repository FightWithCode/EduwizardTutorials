from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from pages import views as PagesView


urlpatterns = [
    # Examples:
    # url(r'^$', 'EduwizardTutorials.views.home', name='home'),
    url(r'^notes/', include('notes.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', PagesView.IndexView, name="IndexView"),
    url(r'^about/$', PagesView.AboutView, name="AboutView"),
    url(r'^teachers/$', PagesView.TeachersView, name="TeachersView"),
    url(r'^gallery/$', PagesView.GalleryView, name="GalleryView"),
    url(r'^courses/$', PagesView.CoursesView, name="CoursesView"),
    url(r'^blog/$', PagesView.BlogView, name="BlogView"),
    url(r'^contact/$', PagesView.ContactView, name="ContactView"),
    url(r'^notes/$', PagesView.NotesView, name="NotesView"),
    url(r'^thankyou/$', PagesView.SubmitThankView, name="SubmitThankView"),
    # url(r'^join/$', PagesView.JoinQueryView, name="JoinQueryView"),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
