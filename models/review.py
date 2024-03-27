#!/usr/bin/python3
"""Module to define the Review class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Class that defines a review

    Args:
        place_id (str): the id of the place
        user_id (str): the id of the user
        text (str): review text
    """

    __tablename__ = "reviews"
    place_id = Column(String(60), ForeignKey("places.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    text = Column(String(1024), nullable=False)

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
