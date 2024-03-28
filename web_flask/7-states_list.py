#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask, render_template, g
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Generates a list of the states on the '/states_list' route
    """
    states_dct = storage.all(State)
    states_objs = states_dct.values()
    return render_template("7-states_list.html", states=states_objs)


@app.teardown_appcontext
def close_session(exception):
    """Closes the database storage session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
