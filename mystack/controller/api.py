"""
    identity authentication
"""
class Auth(object):
    def __init__(self, app):
        self.app = app
    
    def __call__(self, environ,start_response):
        print environ
        if environ.get('HTTP_X_AUTH_TOKEN') != "liaoyuehua":
            start_response('403 Forbidden', [('Content-type', 'text/html')])
            return ['You are forbidden to view this resource']
        return self.app(environ,start_response)

def auth_filter(app,global_config):
    print app
    print global_config
    return Auth(app)

