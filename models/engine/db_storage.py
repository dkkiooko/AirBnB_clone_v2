#!/usr/bin/python3
""" DBStorage (new storage) """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
import os


class DBStorage:
    """ DBStorage Class """
    __engine = None
    __session = None

    def __init__(self):
        """ init method """
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            os.getenv('HBNB_MYSQL_USER'),
            os.getenv('HBNB_MYSQL_PWD'),
            os.getenv('HBNB_MYSQL_HOST'),
            os.getenv('HBNB_MYSQL_DB')), pool_pre_ping=True)

        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ get all objects stored in db """
        objs = []
        if cls is None:
            Classes = [User, City, State, Place, Review, Amenity]
            try:
                for Class in Classes:
                    objs = objs + self.__session.query(Class).all()
            except Exception:
                pass
        else:
            Class = eval(cls) if type(cls) == str else cls
            objs = self.__session.query(Class).all()
        return {f'{type(obj).__name__}.{obj.id}': obj for obj in objs}

    def new(self, obj):
        """ add object to current database session """
        self.__session.add(obj)

    def save(self):
        """ commit all changes of current database session """
        self.__session.commit()

    def delete(self, obj=None):
        """ delete from current database session """
        if obj:
            self.__session.delete(obj)
            self.save()

    def reload(self):
        """ reloads all data in db """
        Base.metadata.create_all(self.__engine)
        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """ close session"""
        self.__session.close()
