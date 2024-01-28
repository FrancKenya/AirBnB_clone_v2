#!/usr/bin/python3
""" The state module for HBNB """
import models
import os
from sqlalchemy.orm import relationship
from models.city import City
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String


class State(BaseModel, Base):
    """ The State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")

    @property
    def cities(self):
        """ Returns the list of City instances with state_id """
        cities = models.storage.all(City)
        if os.getenv("HBNB_TYPE_STORAGE") == "db":
            return [city for city in cities.values()
                    if city.state_id == self.id]
        else:
            return [city for city in cities.values()
                    if city.state_id == self.id]
