import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship


class Comment(BaseModel, Base):
    """ Class to define behavior and data for comments """

    __tablename__ = 'comments'
    id_book = Column(Integer, nullable=False)
    id_user = Column(Integer, nullable=False)
    text = Column(String(1000), nullable=False)
