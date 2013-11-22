from django.conf.urls.defaults import patterns, include, url
from views import logout_page
from portal.views import main_page

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    #url(r'^$', 'gestor.views.home', name='home'),
    # url(r'^gestor/', include('gestor.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    #url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

    # Login / logout.
    (r'^login/$', 'django.contrib.auth.views.login'),
    (r'^logout/$', logout_page),

    #Main
    (r'^$', main_page),

    # Web portal.
    #(r'^portal/', include('portal.urls')),

    # Serve static content.
    (r'^static/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': 'static'}),

)
