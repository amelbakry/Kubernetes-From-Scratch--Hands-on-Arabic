import os
from flask import Flask
app = Flask(__name__)

VERSION = "1.0.2"
ENV = os.environ['ENV']

@app.route('/')
@app.route('/index')
def index():
    msg = "Welcome to Kubernetes!"
    return '''
<html>
    <head>
        <title>Home Page - Microblog</title>
    </head>
    <body>
        <h1>Hello, ''' + msg + '''</h1>
        <h1>I'm running on ''' + ENV + '''</h1>
    </body>
</html>'''

@app.route('/version')
def version():
    return "The Application Version is: {}".format(VERSION)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
