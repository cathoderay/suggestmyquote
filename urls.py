from django.conf.urls.defaults import patterns, include, url
import settings


# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'suggestmydomain.views.home', name='home'),
    # url(r'^suggestmydomain/', include('suggestmydomain.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'suggestmyquote.views.home'),
    url(r'^quote/(?P<id>[0-9]+)/?$', 'suggestmyquote.views.quote'),
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', 
        {'document_root': settings.MEDIA_ROOT}),
)

