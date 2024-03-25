#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def greeting():
    """ Generates 'Hello HBNB!' text on the root route
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Generates 'HBNB' text on the '/hbnb' route
    """
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
