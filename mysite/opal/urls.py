from django.conf.urls import patterns, url
from opal import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^about/$', views.about, name='about'),
    url(r'^people/$', views.people, name='people'),
)
