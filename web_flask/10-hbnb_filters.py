#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask, render_template
from models import storage
from models.amenity import Amenity
from models.state import State

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """Displayes the landing page of HBnB with the states and cities
    """
    states_dct = storage.all(State)
    amenities_dct = storage.all(Amenity)
    return render_template(
            "10-hbnb_filters.html",
            states=states_dct.values(),
            amenities=amenities_dct.values(),
            )


@app.teardown_appcontext
def close_session(exception):
    """Closes the database storage session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
