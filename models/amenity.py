#!/usr/bin/python3
"""Module to define the Amenity class
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """Class that defines an amenity

    Args:
        name (str): the amenity name
    """
    name = ""

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
