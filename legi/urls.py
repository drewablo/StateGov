from django.conf.urls import patterns, include, url
from legi import views

urlpatterns = patterns('',
    url(r'^$', views.get_bill_count, name='get_bill_count')
)