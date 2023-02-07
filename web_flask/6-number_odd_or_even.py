#!/usr/bin/python3
""" flask app """
from flask import Flask, render_template
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


@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def display_python(text):
    """ displays text with a default value in variable """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def display_n(n):
    """ displays an integer """
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def display_html(n):
    """ renders template """
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_oddeven(n):
    """ displays whether entry is even or odd """
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", n=f"{n} is even")
    else:
        return render_template("6-number_odd_or_even.html", n=f"{n} is odd")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
