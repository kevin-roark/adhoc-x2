import os
import sys
import site

os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'
os.environ['PYTHON_EGG_CACHE'] = '/var/.python_eggs'

#site.addsitedir('/home/udbhav/adhoc-env/lib/python2.6/site-packages')
sys.path.append('/var/adhoc')

import django.core.handlers.wsgi
_application = django.core.handlers.wsgi.WSGIHandler()

def application(environ, start_response):
        environ['wsgi.url_scheme'] = environ.get('HTTP_X_URL_SCHEME', 'http')
        return _application(environ, start_response)
