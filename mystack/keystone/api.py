from webob import Response
from webob import exc
from webob import Request

class keystoneController(object):
    def __init__(self):
        pass
    
    def __call__(self, environ, start_response):
        resp = Response("This is the response message from keystone!")
        return resp(environ, start_response)
    
def keystone_factory(global_config, **local_config):
    print '[DEBUG] call keystone_factory'
    return keystoneController()

