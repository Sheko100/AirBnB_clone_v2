#!/usr/bin/python3
"""Module that start Flask app
"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_state(states=storage.all()):
    """Displays list of cities on '/cities_by_states' route
    """
    return render_template("8-cities_by_states.html", states=states)


@app.teardown_appcontext
def shutdown():
    """Closes the session
    """
    storage.close()
