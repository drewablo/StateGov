from django.conf.urls import patterns, include, url
from legi import views

urlpatterns = [
    url(r'^$', views.billcount, name='billcount'),
    url(r'^signed$', views.billnum, name='billnumbers'),
    url(r'^waitingforgov$', views.billwait, name='waitingforgov'),
    url(r'^waitingforlegi$', views.billlegi, name='waitingforlegi'),
]
