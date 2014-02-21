from datetime import datetime, timedelta

from django import template

from adhoc_calendar.models import *

register = template.Library()

def format_time(tim):
    hour = str(tim.hour % 12)
    minutes = tim.strftime('%M %p').lower()
    return hour + ':' + minutes


@register.simple_tag
def event_box(event):
    all_html = []

    open_html = '<div class="event-box">'
    all_html.append(open_html)

    month = event.start_time.strftime('%b');
    dow = event.start_time.strftime('%a');
    day = event.start_time.strftime('%d');
    badge = '<div class="event-date-badge">' + dow + '<hr>' + month + ' ' + day + '</div>'
    all_html.append(badge);

    all_html.append('<div class="event-header">')

    title = '<div class="event-title">' + event.title + '</div>'
    all_html.append(title)

    where = '<div class="event-venue">' + event.venue + '</div>'
    all_html.append(where)

    addr = '<div class="event-address">' + event.address + '</div>'
    all_html.append(addr);

    when = '<div class="event-time">' + format_time(event.start_time)
    if (event.end_time):
        when += ' - ' + format_time(evet.end_time)
    all_html.append(when)

    if (event.url1):
        link = ' <span class="event-linker"><a target="_blank" href="' + event.url1 + '">' + event.link_name1 + '</a></span>'
        all_html.append(link);

    if (event.url2):
        link = ''
        if (event.url1):
            link += ' | '
        link += ' <span class="event-linker"><a target="_blank" href="' + event.url2 + '">' + event.link_name2 + '</a></span>'
        all_html.append(link);

    all_html.append('</div>') # for event-time

    all_html.append('</div>'); # for event-header

    if (event.details or event.image):
        all_html.append('<hr>')

    if (event.image):
        image = '<div class="event-image"><a target="_blank" href="' + event.image.default_image.url + '">' + \
                '<img src="' + event.image.default_image.url + '" alt="' + event.image.title + '"></a>'
        if (event.image.caption):
          image += '<div class="event-image-caption">' + event.image.caption + '</div>'
        image += '</div>'
        all_html.append(image)

    if (event.details):
        details = '<div class="event-description">' + event.details + '</div>'
        all_html.append(details)

    all_html.append('</div>')
    return ''.join(all_html)
