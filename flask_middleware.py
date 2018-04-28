try:
    from urllib.parse import urlencode
except ImportError:
    from urllib import urlencode

class MiddlewareEnviron(object):
    def __init__(self,wsgi,func):
        self.wsgi = wsgi
        self.environ_function = func

    def __call__(self,environ,start_response):
        environ = self.environ_function(environ)
        return self.wsgi(environ,start_response)

class Middleware(object):
    ARGS = 'QUERY_STRING'

    def __init__(self,app=None):
        self.middlewareFunction = None
        self.app = app
        self.middlewareEnvironClass = MiddlewareEnviron

    @staticmethod
    def encode(iterable):
        return urlencode(iterable)

    def init_app(self,app):
        self.app = app

    def middlewareEnviron(self,func):
        self.middlewareFunction = func
        self.app.wsgi_app = self.middlewareEnvironClass(self.app.wsgi_app,self.middlewareFunction)
