from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
from haystack.query import SearchQuerySet
from haystack.views import SearchView

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

sqs = SearchQuerySet().order_by('-timestamp')

urlpatterns = patterns(
    '',
    # Examples:
    # url(r'^$', 'src.views.home', name='home'),
    # url(r'^src/', include('src.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    (r'^music/', include('music.urls')),
    (r'^search/', SearchView(searchqueryset=sqs)),
    (r'^ads/', include('advertising.urls')),
    (r'^events/', include('adhoc_calendar.urls')),
    (r'^', include('blog.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(.*)$', 'django.views.static.serve', kwargs={'document_root': settings.MEDIA_ROOT}),
        (r'^500/$', 'django.views.generic.simple.direct_to_template', {'template': '500.html'}),
        (r'^404/$', 'django.views.generic.simple.direct_to_template', {'template': '404.html'}),
    )
