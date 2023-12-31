#!/usr/bin/python3
"""Module to define the Review class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Class that defines a review

    Args:
        place_id (str): the id of the place
        user_id (str): the id of the user
        text (str): review text
    """
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """Initializes the instance

        Args:
            args: positional arguments
            kwargs: named arguments
        """
        if (len(args) > 0):
            args_dct = args[0]
            for key in args_dct:
                atrbs = self.__dir__()
                if key in atrbs:
                    setattr(self, key, args_dct[key])
        if len(kwargs) < 1:
            super().__init__()
        else:
            super().__init__(**kwargs)
