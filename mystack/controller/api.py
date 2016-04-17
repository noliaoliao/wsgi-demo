"""
    identity authentication
"""
from webob import exc

class Auth(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print environ
        if environ.get('HTTP_X_AUTH_TOKEN') != "liaoyuehua":
            #start_response('403 Forbidden', [('Content-type', 'text/html')])
            #return ['You are forbidden to view this resource']
            return exc.HTTPForbidden()
        return self.app(environ, start_response)
   
    @classmethod
    def factory(cls, app, global_confgi):
        return cls(app)

class IPAddr(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        if environ.get('REMOTE_ADDR').startswith('10.166.224') == False:
            return exc.HTTPForbidden()
        return self.app(environ, start_response)            
    
    @classmethod
    def factory(cls, app, global_config):
        print '[DEBUG]', app
        print '[DEBUG]', global_config 
        return cls(app)          
        
#def auth_filter(app,global_config):
#    return Auth(app)

#def ipaddr_filter(app, global_config):
#    print '[DEBUG]', app
#    print '[DEBUG]', global_config 
#    return IPAddr(app)
