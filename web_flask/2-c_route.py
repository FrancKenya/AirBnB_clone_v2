#!/usr/bin/python3
""" This module uses Flask to run function with specified routes """


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """ Function matched to the route that displays 'Hello HBNB!' """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """ Function matched to route '/hbnb' and displays 'HBNB' """

    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def show_c(text):
    """ Function matched to route '/c/<text>' that displays C
    followed by a space and text """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
