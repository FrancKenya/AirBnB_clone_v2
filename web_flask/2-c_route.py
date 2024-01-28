#!/usr/bin/python3

"""
Starts a flask web application
The web applicatin is listening on 0.0.0.0, port 5000
Uses the option strict_slashes=False in route definition
"""


from flask import Flask
app = Flask(__name__)
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ displays hello hbnb string """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def display_hbnb():
    """ displays HBNB """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def show_c(text):
    """ dispays "C" followed by the value of the text variable """
    text = text.replace('_', ' ')
    return 'C {}'.format(text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
