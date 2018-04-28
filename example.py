from flask import Flask,request
from flask_middleware import Middleware

app = Flask(__name__)
middleware = Middleware(app)

@middleware.middlewareEnviron
def middle(environ):
    args = Middleware.encode({'name':'value'})
    environ[Middleware.ARGS] = args
    return environ

@app.route('/',methods=['GET'])
def index():
    print(request.args)
    return 'hi'

app.run(debug=True)

