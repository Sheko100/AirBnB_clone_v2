#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Generates a list of cities by states on the '/cities_by_states' route
    """
    states_dct = storage.all(State)
    states_objs = states_dct.values()
    return render_template("8-cities_by_states.html", states=states_objs)


@app.teardown_appcontext
def close_session(exception):
    """Closes the database storage session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
