from datetime import datetime, timedelta

from django import template

from adhoc_calendar.models import *

register = template.Library()

@register.simple_tag
def event_box(event):
    open_html = '<div class="event-box'
    if (event.url):
        open_html += ' event-box-link"><a href="' + event.url + '" target="_blank"</a>'
    else:
        open_html += '">'
    all_html = [open_html]

    if False:#(event.url):
        title = '<div class="event-title"><a target="_blank" href="' + event.url + '">' + event.title + '</a></div>'
    else:
        title = '<div class="event-title">' + event.title + '</div>'
    all_html.append(title)

    when = '<div class="event-time">' + event.start_time.strftime('%B %d. %I:%M %p')
    if (event.end_time):
        when += event.end_time.strftime('- %I:%M %p')
    when += '</div>'
    all_html.append(when)

    where = '<div class="event-venue">@ ' + event.venue + '</div>'
    all_html.append(where)

    if (event.image):
        image = '<div class="event-image"><img src="' + event.image.default_image.url + '" alt="' + event.image.title + ">"
        if (event.image.caption):
            image += '<p>' + event.image.caption + '</p>'
        image += '</div>'
        all_html.append(image)

    if (event.details):
        details = '<hr><div class="event-description">' + event.details + '</div>'
        all_html.append(details)

    if (event.url):
        close_html = '</a></div>'
    else:
        close_html = '</div>'

    all_html.append(close_html)
    return ''.join(all_html)