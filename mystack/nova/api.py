"""
    nova api router
"""

from webob import Response
from webob import Request
from webob.dec import *
from routes import Mapper, middleware

class APIRouter(object):
    def __init__(self):
        print '___init____'
        self._setup_routes()
    
    @wsgify
    def __call__(self, req):
        return self.router
    
    def _setup_routes(self):
        mapper = Mapper()
        mapper.connect(None,'/{opname}/{action}',conditions={'method':['GET']})
        mapper.redirect('','/servers/detail')
        self.router = middleware.RoutesMiddleware(self.dispatch, mapper)
    
    @wsgify
    #def dispatch(self, environ, start_response):
    def dispatch(self, req):
        print req.environ['wsgiorg.routing_args'][1]
        return 'OK OK OK'

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls()
    
def nova_factory(global_config, **local_config):
    print '[DEBUG] call nova_factory'
    return novaController()

