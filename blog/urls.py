from django.conf.urls.defaults import *
from django.contrib.auth.decorators import login_required, permission_required
from django.conf import settings

from blog.views import *

urlpatterns = patterns(
    '',
    (r'^images/$', login_required(ImageList.as_view()), {}, 'images'),
    (r'^images/new/$', new_image, {}, 'new_image'),
    (r'^tag/(?P<tag>[-\w]+)/$', PostsByTag.as_view(), {}, 'posts_by_tag'),
    (r'^author/(?P<user_id>\d+)/$', PostsByAuthor.as_view(), {}, 'posts_by_author'),
    (r'^feed/$', AllEntriesFeed(), {}, 'rss_feed'),
    (r'^(?P<slug>[-\w]+)/$', PostDetail.as_view(), {}, 'post'),
    (r'^$', HomeView.as_view(), {}, 'home'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
   )
