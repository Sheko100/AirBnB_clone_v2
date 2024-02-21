#!/usr/bin/python3
"""Module to define the Place class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, Float, ForeignKey


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
        if len(kwargs) < 1:
            super().__init__()
        else:
            super().__init__(**kwargs)
