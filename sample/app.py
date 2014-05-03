from wsgiref.simple_server import make_server

def myapp(environ, start_response):
    body = []
    headers = [('Content-Type', 'text/plain')]
    start_response('200 OK', headers)
    return body

srv = make_server('localhost', 8000, myapp)
srv.serve_forever()
