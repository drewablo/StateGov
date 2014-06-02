from django.conf.urls import patterns, include, url
from legi import views

urlpatterns = patterns('',
    url(r'^$', views.billcount, name='billcount')
)
