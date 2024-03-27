#!/usr/bin/python3
"""Module for the database storage
"""

import importlib
import os
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session


class DBStorage:
    """represents a database storage object

    Attributes:
        __engine (obj): sqlalchemy engine insatnce
        __session (obj): connection sesssion with the database
    """

    __engine = None
    __session = None

    def __init__(self):

        username = os.getenv("HBNB_MYSQL_USER")
        pwd = os.getenv("HBNB_MYSQL_PWD")
        host = os.getenv("HBNB_MYSQL_HOST")
        db = os.getenv("HBNB_MYSQL_DB")
        url = "mysql+mysqldb://{}:{}@{}/{}".format(username, pwd, host, db)

        self.__engine = create_engine(url, pool_pre_ping=True)

        if os.getenv("HBNB_ENV") == "test":
            from models.base_model import Base
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Gets a dictionary of objects based on the cls value or
        all objects if cls is None

        Args:
            cls (class): class to filter the objects

        Returns:
            a dictionary of objects
        """

        modules = ["user", "state", "city", "amenity", "place", "review"]
        dct = {}
        Session = self.__session
        session = Session()
        pkg = "models.engine"

        if cls:
            model_name = cls.__name__
            model_path = "..{}".format(model_name.lower())
            module = importlib.import_module(model_path, pkg)
            model = getattr(module, model_name.capitalize())
            for instance in session.query(model).all():
                key = "{}.{}".format(cls, instance.id)
                dct[key] = instance
        else:
            for name in modules:
                from models.base_model import Base
                model_path = "..{}".format(name)
                module = importlib.import_module(model_path, pkg)
                model = getattr(module, name.capitalize())
                if issubclass(model, Base):
                    cls_name = model.__name__
                    for instance in session.query(model).all():
                        key = "{}.{}".format(cls_name, instance.id)
                        dct[key] = instance
        return dct

    def new(self, obj):
        """Adds the object obj to the current database session
        """
        Session = self.__session
        session = Session()
        session.add(obj)

    def save(self):
        """Commits all the changes to the current database session
        """
        Session = self.__session
        session = Session()
        session.commit()

    def delete(self, obj=None):
        """deletes from the current database session obj if not None
        """
        if obj:
            Session = self.__session
            session = Session()
            session.delete(obj)

    def reload(self):
        """creates all the database tables, then creates a session
        """

        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        from models.base_model import Base

        Base.metadata.create_all(self.__engine)
        session_fac = sessionmaker(self.__engine, expire_on_commit=False)
        Session = scoped_session(session_fac)
        self.__session = Session

    def close(self):
        """Closes the database sessions
        """
        session = self.__session
        session.remove()
