import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship


class User(BaseModel, Base):
    """ Class to define behavior and data for users """

    __tablename__ = 'users'
    username = Column(String(45), nullable=False)
    password = Column(String(45), nullable=False)
    first_name = Column(String(45), nullable=False)
    last_name = Column(String(45), nullable=False)

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)
