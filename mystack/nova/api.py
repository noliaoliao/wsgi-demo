from webob import Response
from webob import exc
from webob import Request

class novaController(object):
    def __init__(self):
        pass
    
    def get_data(self, environ):
        print 'get_data'
        try:
            content_len = environ.get('CONTENT_LENGTH')
        except(ValueError):
            content_len = 0
        if content_len > 0:
            print content_len
            content_data = environ.get('wsgi.input').read(content_len)
            print content_data
            open('data','w').write(content_data)
        #print 'xxxx'
    
    def __call__(self, environ, start_response):
        #if environ.get('REQUEST_METHOD') == "POST":
        #    self.get_data(environ)
        req = Request(environ)
        print req.path_info
        resp = Response("This is the response message from nova!")
        return resp(environ, start_response)
    
def nova_factory(global_config, **local_config):
    print '[DEBUG] call nova_factory'
    return novaController()

