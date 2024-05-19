#!/usr/bin/python3
"""
This script starts Flask and makes a web application listen on
on 0.0.0.0:5000
"""
from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_bnb():
    """ The Route displaying Hello HBNB! """
    return 'Hello HBNB!'


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
