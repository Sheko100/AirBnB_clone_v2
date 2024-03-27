#!/usr/bin/python3
"""Module to define the Place class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
import models


# a Many-To-Many relationship between Place and Amenity tables
places_amenities = Table(
        "place_amenity",
        Base.metadata,
        Column(
            "place_id",
            String(60),
            ForeignKey("places.id"),
            primary_key=True,
            nullable=False),
        Column(
            "amenity_id",
            String(60),
            ForeignKey("amenities.id"),
            primary_key=True,
            nullable=False)
        )


class Place(BaseModel, Base):
    """Class that defines a place

    Args:
        city_id (str): the id of the City
        user_id (str); the id of the User
        name (str): the place name
        description (str): the place description
        number_rooms (int): the number of rooms
        number_bathrooms (int): the number of bathrooms
        max_guest (int): maximum number of guests
        price_by_night (int): the price of the night
        latitude (float): the place latitude
        longitude (float): the place longitude
        amenity_ids (list): list of Amenity ids
    """

    __tablename__ = 'places'

    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=True)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    # relationships
    reviews = relationship(
            "Place",
            backref="place",
            cascade="all, delete, delete-orphan")

    amenities = relationship(
            "Amenity",
            secondary="place_amenity",
            viewonly=False)

    def __init__(self, *args, **kwargs):
        """Initializes the instance

        Args:
            args: positional arguments
            kwargs: named arguments
        """
        if len(args) > 0:
            args_dct = args[0]
            for key in args_dct:
                atrbs = self.__dir__()
                if key in atrbs:
                    setattr(self, key, args_dct[key])

        dir_dct = self.__dir__()
        for key in kwargs:
            if key in dir_dct:
                self.__dict__[key] = kwargs[key]
        super().__init__(**kwargs)

    @property
    def reviews(self):
        """ Getter method for reviews. It returns a list of Review instaces
        with place_id equals to the current Place.id """

        reviews = models.storage.all(Review).values()

        # for each review in reviews, return reviews that belong to the
        # current Place instance
        reviews_list = [
                review for review in reviews if self.id == review.place_id
                ]

        return reviews_list

    @property
    def amenities(self):
        """ returns a list of Amenity instances based on the
        attribute amenity_ids, that contains all amenities linked to a Place
        """

        amenities = models.storage.all(Amenity).values()

        amenities_list = [
                amenity for amenity in amenities
                if self.id in self.amenity_ids
                ]

        return amenities_list

    @amenities.setter
    def amenities(self, amenity_obj):
        """ handles append method for adding an amenity to
        the amenity_ids list.
        Should only accept Amenity object, otherwise do nothing """

        if isinstance(amenity_obj, Amenity):
            self.amenity_ids.append(amenity_obj.id)
