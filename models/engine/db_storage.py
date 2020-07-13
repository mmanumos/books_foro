import models
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy import event
from models.base_model import Base
from models.users import User
from models.books import Book
from models.comments import Comment

classes = {"Book": Book, "User": User, "Comment": Comment}


def _fk_pragma_on_connect(dbapi_con, con_record):
    """ enforce Foreign Key constraints for sqlite """
    dbapi_con.execute('pragma foreign_keys=ON')


class DBStorage:
    """ Administration, manipulation and connection for database """
    __session = None  # private attribute to manage session for database
    __engine = None  # private attribute that contains connection configuration

    def __init__(self):
        """ Create the connection bridge with Database """
        self.__engine = create_engine(
            r'sqlite:///intel.db')
        event.listen(self.__engine, 'connect', _fk_pragma_on_connect)

    def reload(self):
        """ Load all data in objects for sqlAlchemy metadata/map to be used by the session """
        Base.metadata.create_all(self.__engine)
        sess_factory = sessionmaker(
            bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(sess_factory)
        self.__session = Session

    def close(self):
        """ remove session of a database """
        self.__session.remove()

    def insert(self, obj):
        """ Add the object to the map/metadata of the sqlalchemy orm """
        self.__session.add(obj)
        self.commit()

    def commit(self):
        """ Insert and update all changes for sqlalchemy map/metadata into database """
        self.__session.commit()

    def delete(self, obj=None):
        """ remove an object of a session and the Database  """
        if obj is not None:
            self.__session.delete(obj)
            self.commit()

    def all(self, cls=None):
        """query on the current database session"""
        new_dict = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.__name__ + '.' + str(obj.id)
                    new_dict[key] = obj
        return (new_dict)

    def get(self, cls, id):
        """
        Returns the object based on the class name and its ID, or
        None if is not found
        """
        if cls not in classes.values():
            return None

        all_cls = models.storage.all(cls)
        for value in all_cls.values():
            if (value.id == int(id)):
                return value
