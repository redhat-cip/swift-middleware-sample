from wsgiref.simple_server import make_server
from sample.middleware import SummitMiddleware

def myapp(environ, start_response):
    body = []
    keys = ['PATH_INFO','QUERY_STRING', 'REQUEST_METHOD', 'HTTP_HEADERNAME', 'wsgi.input']
    for key in keys:
        value = environ.get(key)
        body.append("%s: '%s'\n" % (key, value))
    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    return body

def app_factory(global_config, **local_config):
    return myapp
