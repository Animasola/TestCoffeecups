from django.conf.urls.defaults import patterns, include, url
from testapp.views import main_page_info

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', main_page_info, name='home'),
    # Examples:
    # url(r'^$', 'testingproject.views.home', name='home'),
    # url(r'^testingproject/', include('testingproject.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
