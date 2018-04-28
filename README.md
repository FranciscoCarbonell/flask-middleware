It is a simple way to implement a middleware to our flask application, we can receive the request
in a decorator to modify any data or check.

install
`python setup.py install`

or
`pip install flask-middleware`

**example**
```python
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
```