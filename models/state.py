#!/usr/bin/python3
"""Module to define the State class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models import storage
from models.city import City


class State(BaseModel, Base):
    """Class that defines a State

    Attributes:
        name (str): the state name
    """
    __tablename__ = "states"

    name = Column("name", String(128), nullable=False)
    cities = relationship("City", backref="state")

    def __init__(self, *args, **kwargs):
        """Initializes the instance

        Args:
            args: positional arguments
            kwargs: named arguments
        """
        dir_dct = self.__dir__()
        for key in kwargs:
            if key in dir_dct:
                self.__dict__[key] = kwargs[key]
        super().__init__(**kwargs)

    @property
    def cities(self):
        """gets the cities for the file storage
        """
        all_cities = storage.all(City)
        city_objs = all_cities.values()
        self.__cities = [
                city for city in city_objs if city.state_id == self.id
                ]
        return self.__cities
