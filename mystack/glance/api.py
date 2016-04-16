from webob import Response
from webob import exc
from webob import Request

class glanceController(object):
    def __init__(self):
        pass

    def get_data(self, environ):
        print 'get_data'
        try:
            content_len = environ.get('CONTENT_LENGTH')
        except(ValueError):
            content_len = 0
        if content_len > 0 and content_len < 1025:
            content_data = environ.get('wsgi.input').read(content_len)
            print content_data
            open('glancedata','w').write(content_data)
    
    def __call__(self, environ, start_response):
        resp = Response("This is the response message from glance!")
        return resp(environ, start_response)
    
def glance_factory(global_config, **local_config):
    print '[DEBUG] call glance_factory'
    return glanceController()

