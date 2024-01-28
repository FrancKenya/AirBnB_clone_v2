#!/usr/bin/python3

"""
A module that has the database storage class that helps to store date
in a database
"""
import os
from sqlalchemy import create_engine
from models.user import User
from models.review import Review
from models.amenity import Amenity
from models.place import Place
from models.base_model import BaseModel, Base
from models.state import State
from models.city import City
from sqlalchemy.orm import scoped_session, sessionmaker


class DBStorage():
    """
    A class that allowsthe data storage in a relational database
    """
    __engine = None
    __session = None

    def __init__(self):
        """initializes a new database session"""
        user, pword, host, db, env = (
                os.getenv("HBNB_MYSQL_USER"),
                os.getenv("HBNB_MYSQL_PWD"),
                os.getenv("HBNB_MYSQL_HOST"),
                os.getenv("HBNB_MYSQL_DB"),
                os.getenv("HBNB_ENV")
                )
        self.__engine = create_engine(
                "mysql+mysqldb://{}:{}@{}/{}"
                .format(user, pword, host, db), pool_pre_ping=True)
        Session = sessionmaker(bind=self.__engine)
        self.__session = Session()
        if env == "test":
            Base.metadata.drop_all()

    def all(self, cls=None):
        """ checks the current database sessionall objects """
        result = {}
        if cls:
            for obj in self.__session.query(cls).all():
                key = "{}.{}".format(cls.__name__, obj.id)
                result[key] = obj
        else:
            classes = [User, State, City, Amenity, Place, Amenity]
            for cls in classes:
                for obj in self.__session.query(cls).all():
                    key = "{}.{}".format(type(obj).__name__, obj.id)
                    result[key] = obj
        return result

    def new(self, obj):
        """ Adds object to the current database session """
        self.__session.add(obj)

    def save(self):
        """ Commits changes of the current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ Delete from the current database session """
        if obj:
            self.__session.delete(obj)

    def reload(self):
        """ Restarts the session """
        Base.metadata.create_all(self.__engine)
        Session = sessionmaker(self.__engine, expire_on_commit=False)
        self.__session = Session()

    def close(self):
        """close connection to the database on each web request"""
        self.__session.close()
