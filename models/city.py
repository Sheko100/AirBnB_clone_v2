#!/usr/bin/python3
"""Module to define the City class
"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship


class City(BaseModel, Base):
    """Class that defines a city

    Attributes:
        __tablename__ (str): the table name
        state_id (str): the id of the State instance
        name (str): the city name
    """
    __tablename__ = "cities"

    state_id = Column(
            "state_id",
            String(60),
            ForeignKey("states.id"),
            nullable=False
            )
    name = Column("name", String(128), nullable=False)

    # relationships
    places = relationship(
            "Place",
            backref="cities",
            cascade="all, delete, delete-orphan")

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
