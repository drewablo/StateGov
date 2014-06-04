from django.conf.urls import patterns, include, url
from legi import views

urlpatterns = [
    url(r'^$', views.billcount, name='billcount'),
    url(r'^bills/$', views.billnum, name='billnumbers')
]
