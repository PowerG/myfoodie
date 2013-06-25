from Restaurant.views import *
from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

urlpatterns = patterns('',
(r'^$',index),
(r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),

(r'^search$',search),
(r'^/search/item$',item),



)
