#!/usr/bin/python3
""" This module uses Flask to run function with specified routes """


from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """ Function matched to the route that displays 'Hello HBNB! """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Function matched to route '/hbnb' and displays 'HBNB' """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def display_c(text):
    """ Function matched to route '/c/<text>' that displays C
    followed by a space and text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


# Handles route ending at both the variable and static part
@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def display_py_text(text='is cool'):
    """ displays "Python " followed by text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Route that displays "n is a number" if n is an integer"""
    return '{} is a number'.format(n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
