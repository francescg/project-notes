from django.conf.urls.defaults import patterns, include, url
from portal import views

urlpatterns = patterns('',
    # Examples:
 
    (r'^$', portal.views.main),


)
