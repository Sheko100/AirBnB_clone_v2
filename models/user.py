#!/usr/bin/python3
"""Module to define the User class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.place import Place
from models.review import Review

class User(BaseModel, Base):
    """Class that defines a User

    Attributes:
        email (str): the user email
        password (str): the user password
        first_name (str): the user first name
        last_name (str): the user last name
    """

    __tablename__ = "users"

    email = Column("email", String(128), nullable=False)
    password = Column("password", String(128), nullable=False)
    first_name = Column("first_name", String(128), nullable=True)
    last_name = Column("last_name", String(128), nullable=True)

    # relationships
    places = relationship(
            "Place",
            backref="user",
            cascade="all, delete, delete-orphan")

    reviews = relationship(
            "Review",
            backref="user",
            cascade="all, delete, delete-orphan")

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
