#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask, render_template
from markupsafe import escape

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


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """ Generates text appended to 'C ' on the '/c/<text>' route
    """
    return f"C {escape(text.replace('_', ' '))}"


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python(text="is_cool"):
    """ Generates text appended to 'Python ' if there is a text passed
    otherwise 'Python is cool'on the '/python/(<text>)' route
    """
    return f"Python {escape(text.replace('_', ' '))}"


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """ Generates '<n> is a number' on the '/number/<n>' route
    """
    return f"{escape(n)} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_page(n):
    """ Returns an html page with generated number
    on the '/number_template/<int:n>' route
    """
    return render_template("5-number.html", num=n)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
