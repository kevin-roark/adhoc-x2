from django.conf.urls.defaults import *
from django.conf import settings


from adhoc_calendar.views import *

urlpatterns = patterns(
    '',
    (r'^$', upcoming_events, {}, 'upcoming_events'),
    (r'^(?P<year>\d\d\d\d)/(?P<month>\d\d)$', events_in_month, {}, 'monthly_events'),
)