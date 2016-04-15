class Auth(object):
    def __inti__(self, app):
        self.app = app
    
    def __call__(self, environ, start_response):
        print 'filter auth'
        return self.app(environ, start_response)

def auth_filter(app, global_config, **local_config):
    return Auth(app)

