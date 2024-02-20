#!/usr/bin/python3
"""Module to define the City class
"""
from models.base_model import BaseModel


class City(BaseModel):
    """Class that defines a city

    Args:
        state_id (str): the id of the State instance
        name (str): the city name
    """
    state_id = ""
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
            if "state_id" in args_dct:
                self.state_id = args_dct["state_id"]
        if len(kwargs) < 1:
            super().__init__()
        else:
            super().__init__(**kwargs)
