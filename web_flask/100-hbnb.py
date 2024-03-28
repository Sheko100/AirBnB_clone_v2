#!/usr/bin/python3
"""Module that creates a flask app
"""

from flask import Flask, render_template
from markupsafe import escape
from models import storage
from models.amenity import Amenity
from models.place import Place
from models.state import State
from models.user import User

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Displayes the landing page of HBnB with the states and cities
    """
    states_dct = storage.all(State)
    amenities_dct = storage.all(Amenity)
    places_dct = storage.all(Place)
    users_dct = storage.all(User)
    return render_template(
            "100-hbnb.html",
            states=states_dct.values(),
            amenities=amenities_dct.values(),
            places=places_dct.values(),
            users=users_dct.values()
            )


@app.teardown_appcontext
def close_session(exception):
    """Closes the database storage session
    """
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
