#!/usr/bin/python3
"""Module to define a BaseModel class"""

from datetime import datetime
from models import storage
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime
from uuid import uuid4

Base = declarative_base()


class BaseModel:
    """A class to define a base model

    Attributes:
        id: object id
        created_at: the date and time of object creation
        updated_at: the data and time of object updating
    """

    id = Column("id", String(60), primary_key=True, nullable=False)
    created_at = Column(
            "created_at",
            DateTime(),
            nullable=False,
            default=datetime.utcnow()
            )
    updated_at = Column(
            "updated_at",
            DateTime(),
            nullable=False,
            default=datetime.utcnow()
            )

    def __init__(self, *args, **kwargs):
        """initializes the instance of the BaseModel

        Args:
            args: positional arguments
            kwargs: named arguments
        """

        """
        if len(kwargs) > 0:
            dir_dct  = self.__dir__()
            for key in kwargs:
                if key in dir_dct:
                    self.__dict__[key] = kwargs[key]
            #self.__dict__ = kwargs
            dct = self.__dict__
            if "__class__" in dct:
                del dct["__class__"]
            print(dct)
            dct["created_at"] = datetime.fromisoformat(dct["created_at"])
            dct["updated_at"] = datetime.fromisoformat(dct["updated_at"])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        """
        if 'id' in kwargs:
            dir_dct = self.__dir__()
            dct = self.__dict__
            for key in kwargs:
                if key in dir_dct and key != "__class__":
                    self.__dict__[key] = kwargs[key]
            dct["created_at"] = datetime.fromisoformat(dct["created_at"])
            dct["updated_at"] = datetime.fromisoformat(dct["updated_at"])
        else:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()

    def __str__(self):
        cls_name = self.__class__.__name__

        return "[{}] ({}) {}".format(cls_name, self.id, self.__dict__)

    def save(self):
        """Updates the updated_at attribute with the current datetime
        """

        self.updated_at = datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """Creates a dictionary for the instance
        """

        dct = self.__dict__.copy()
        dct["__class__"] = self.__class__.__name__
        dct["created_at"] = dct["created_at"].isoformat()
        dct["updated_at"] = dct["updated_at"].isoformat()
        if '_sa_instance_state' in dct:
            del dct['_sa_instance_state']

        return dct

    def delete(self):
        """Deletes this object from the storage
        """
        storage.delete(self)
