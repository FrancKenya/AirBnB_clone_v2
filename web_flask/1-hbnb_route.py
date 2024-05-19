#!/usr/bin/python3
""" Starts a web application with certain routes"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Fuction matched to the route that displays 'Hello HBNB!' """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ Function matched to  route '/hbnb' and displays 'HBNB' """

    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
