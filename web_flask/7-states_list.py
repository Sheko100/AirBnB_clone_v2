#!/usr/bin/python3
"""Module that start Flask app
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def states_list(states=storage.all()):
    """Displays list of states on '/states_list' route
    """
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def shutdown():
    """Closes the session
    """
    storage.close()
