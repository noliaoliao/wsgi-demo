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
        #print 'novaController'
        #status = '200 OK'
        #response_headers = [('Content-Type', 'text/html')]
        #start_response(status, response_headers)
        #return ['response mesage from nova.']
        if environ.get('REQUEST_METHOD') == "POST":
            self.get_data(environ)
        resp = Response("this is the response message!")
        return resp(environ, start_response)
    
def nova_factory(global_config, **local_config):
    print 'helo'
    return novaController()

