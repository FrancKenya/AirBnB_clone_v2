#!/usr/bin/python3
""" This module uses Flask to run function mapped with specified routes """


from flask import Flask, render_template

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
    """ Displays C followed by the value of the text variable """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def display_py_text(text='is cool'):
    """ displays "Python " followed by text """
    text = text.replace('_', ' ')
    return 'Python {}'.format(text)


@app.route('/number/<int:n>', strict_slashes=False)
def show_number(n):
    """Route that displays "n is a number" if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def show_number_template(n):
    """ If n is an int it displays a HTML page """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def display_number_odd_or_even(n):
    """
    Displays an HTML page only if n is an integer:
        H1 tag:
            "Number: n is even or odd"
    """
    return render_template('6-number_odd_or_even.html', number=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
