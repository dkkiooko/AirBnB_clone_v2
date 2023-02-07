#!/usr/bin/python3
""" add new routing method with variable"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_world():
    """ displays text """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ displays text """
    return "HBNB"


@app.route('/c/<string:text>', strict_slashes=False)
def display_c(text):
    """ display variable """
    return 'C {}'.format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
