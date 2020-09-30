# import Flask object from flask package
from flask import Flask
# configure flask application instance with the name 'app'
app = Flask(__name__)

# handle incoming web request and send responses to the user

# turns a python function into a flask view function, which converts the functions return value into an HTTP response to be displayed by an HTTP client, such as a web browser

# '/' passed in to signify that this function will respond to web request for the URL /


@app.route('/')
def hello():
    return 'Hello, world!'
