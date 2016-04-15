class novaController(object):
    def __init__(self):
        pass
    
    def __call__(self, environ, start_response):
        #print 'novaController'
        status = '200 OK'
        response_headers = [('Content-Type', 'text/html')]
        start_response(status, response_headers)
        return ['response mesage from nova.']

def nova_factory(global_config, **local_config):
    print 'helo'
    return novaController()

