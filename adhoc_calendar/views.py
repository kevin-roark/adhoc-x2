from datetime import datetime, date, timedelta

from django.views.generic import DetailView, ListView
from django.utils.decorators import method_decorator
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response
from django.template import RequestContext
from taggit.models import Tag

from adhoc_calendar.models import *

def render_short(request, template, data):
    return render_to_response(template, data, context_instance=RequestContext(request))

def upcoming_events(request):
    """ all future events """
    yesterday = datetime.now() - timedelta(days=1) # pretend its yesterday to show all of "tonight's" events
    events = Event.objects.filter(start_time__gte=yesterday).order_by('start_time')
    context = {'events': events}
    return render_short(request, 'adhoc_calendar/events.html', context)

def events_in_month(request, year, month):
    """ Year in 'xxxx' format and month in 'yy' format """
    month = datetime(year=year, month=month, day=1)
    next_month = month + timedelta(months=1)
    month_events = Event.objects.filter(start_time__gte=month, start_time__lte=next_month).order_by('start_time')
    return False