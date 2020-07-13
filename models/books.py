import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer
from sqlalchemy.orm import relationship
from models.comments import Comment


class Book(BaseModel, Base):
    """ Class to define behavior and data for books """

    __tablename__ = 'books'
    title = Column(String(80), nullable=False)
    publication_date = Column(String(80), nullable=False)
    comments = relationship("Book", backref="Comment")

    def __init__(self, **kwargs):
        """ constructor sends the values for the object to be created from BaseModel """
        BaseModel.__init__(self, **kwargs)

    @property
    def comments(self):
        all_comments = models.storage.all(Comment)
        book_comments = []
        for key, value in all_comments.items():
            if self.id == value.id_book:
                book_comments.append(value)
        return book_comments
