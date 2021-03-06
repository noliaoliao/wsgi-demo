"""
    nova api router
"""

from webob import Response
from webob import Request
from webob.dec import *
from routes import Mapper, middleware
from client import MySQLClient
import random
import string
import uuid
import md5
import json

# nova controller class
class Controller(object):
    def __init__(self):
        self.client = MySQLClient(host='localhost', db='mystack', user='root', passwd='liao123')
        print '[DEBUG] Controller class init.'
    
    def detail(self):
        print '[DEBUG] call controller.detail.'
        #return "{'detail':{'name':'host-01','ID':'001'}}\n"
        sql = "select uid, username,userpasswd from user"
        self.client.execute(sql)
        details = self.client.fetchall()
        #for eachitem in details:
        #    print eachitem

        return json.dumps(details) 

    def create(self):
        print '[DEBUG] call controller.create'
        id = uuid.uuid4().hex
        username = ''.join(random.sample(string.ascii_letters,8))
        passwd = ''.join(random.sample(string.ascii_letters,8))
        encode = md5.new()
        encode.update(passwd)
        userpasswd = encode.hexdigest()

        sql = "insert into user values(\""+id+"\",\""+username+"\",\""+userpasswd+"\")"
        self.client.execute(sql)

        resp = {}
        resp["ID"] = id
        resp["name"] = username
        resp["passwd"] = userpasswd
        return json.dumps(resp)

    def sayhello(self):
        print '[DEBUG] call controller.sayhello'
        return "hello~\n"
    
    #NOTE(lyh): must add the __call__ function
    #otherwise type(controller) is unicode
    #and raise AttributeError 
    def __call__(self):
        print '[DEBUG] call controller.__call__'

class APIRouter(object):
    def __init__(self):
        print '___init____'
        self.controller = Controller()
        self._setup_routes()
    
    @wsgify
    def __call__(self, req):
        return self.router
    
    def _setup_routes(self):
        mapper = Mapper()
        mapper.redirect('', '/server/detail')
        #mapper.connect(None, '/{opname}/{action}',controller=control, conditions={'method':['GET']})
        mapper.resource('server', 'servers', controller=self.controller)
        self.router = middleware.RoutesMiddleware(self.dispatch, mapper)
    
    @wsgify
    def dispatch(self, req):
        match = req.environ['wsgiorg.routing_args'][1]
        print match
        if not match:
            path = req.environ['PATH_INFO']
            print "[ERROR] error url: ", path
            return "error url: %s" %path
        controller = match['controller']
        #action = match['action']
        id = match['id']
        if hasattr(controller, id):
            func = getattr(controller, id)
            ret = func()
            return ret
        else:
            print "[ERROR] no action named: ", id
            return "no action named: %s" %id      

    @classmethod
    def factory(cls, global_config, **local_config):
        return cls()
    
#def nova_factory(global_config, **local_config):
#    print '[DEBUG] call nova_factory'
#    return novaController()
