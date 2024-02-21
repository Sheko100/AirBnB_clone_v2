#!/usr/bin/python3
"""Module to define the Amenity class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Amenity(BaseModel, Base):
    """Class that defines an amenity

    Args:
        name (str): the amenity name
    """

    __tablename__ = "amenities"

    name = Column(String(128), nullable=False)

    def __init__(self, *args, **kwargs):
        """Initializes the instance

        Args:
            args: positional arguments
            kwargs: named arguments
        """
        if len(args) > 0:
            args_dct = args[0]
            if "name" in args_dct:
                self.name = args_dct["name"]

        if len(kwargs) < 1:
            super().__init__()
        else:
            super().__init__(**kwargs)
