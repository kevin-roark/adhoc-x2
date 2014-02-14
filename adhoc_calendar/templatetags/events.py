from datetime import datetime, timedelta

from django import template

from adhoc_calendar.models import *

register = template.Library()

@register.simple_tag
def event_box(event):
    all_html = []

    open_html = '<div class="event-box'
    if (event.url):
        open_html += ' event-box-link"><a href="' + event.url + '" target="_blank"</a>'
    else:
        open_html += '">'
    all_html.append(open_html)

    month = event.start_time.strftime('%b');
    dow = event.start_time.strftime('%a');
    day = event.start_time.strftime('%d');
    badge = '<div class="event-date-badge">' + dow + '<hr>' + month + ' ' + day + '</div>'
    all_html.append(badge);

    title = '<div class="event-title">' + event.title + '</div>'
    all_html.append(title)

    when = '<div class="event-time">' + event.start_time.strftime('%B %d. %I:%M %p')
    if (event.end_time):
        when += event.end_time.strftime(' - %I:%M %p')
    when += '</div>'
    all_html.append(when)

    where = '<div class="event-venue">@ ' + event.venue + '</div>'
    all_html.append(where)

    if (event.url):
        link = '<div class="event-url">' + event.url + '</div>'
        all_html.append(link);

    if (event.details or event.image):
        all_html.append('<hr>')

    if (event.image):
        image = '<div class="event-image"><img src="' + event.image.default_image.url + '" alt="' + event.image.title + '">'
        if (event.image.caption):
          image += '<div class="event-image-caption">' + event.image.caption + '</div>'
        image += '</div>'
        all_html.append(image)

    if (event.details):
        details = '<div class="event-description">' + event.details + '</div>'
        all_html.append(details)

    if (event.url):
        close_html = '</a></div>'
    else:
        close_html = '</div>'

    all_html.append(close_html)
    return ''.join(all_html)