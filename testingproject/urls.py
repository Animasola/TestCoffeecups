from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from testapp.views import main_page_info, requests_log, edit_my_info

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page_info, name='home'),
    url(r'^requests/', requests_log, name='reqslog'),
    url(r'^editinfo/', edit_my_info, name='editinfo'),
    # Examples:
    # url(r'^$', 'testingproject.views.home', name='home'),
    # url(r'^testingproject/', include('testingproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.STATIC_ROOT}),
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
            {'document_root': settings.MEDIA_ROOT}),
)
