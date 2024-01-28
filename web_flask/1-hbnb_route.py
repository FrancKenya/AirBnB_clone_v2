#!/usr/bin/python3
""" Starts a web application with certain routes"""


from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """ Route displaying the string Hello HBNB """

    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def show_hbnb():
    """ Route displaying HBNB string """

    return "HBNB"


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
