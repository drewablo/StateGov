from django.conf.urls import patterns, include, url


urlpatterns = patterns('',
    url(r'^legi/', include('legi.urls')),
)