#!/usr/bin/python3
"""The base class for the airbnb project"""
import uuid
from datetime import datetime
from . import storage


class BaseModel():

    def __init__(self, *args, **kwargs):
        
        if len(kwargs) > 3:
            self.id = kwargs['id']
            self.created_at = datetime.fromisoformat(kwargs['created_at'])
            self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        string = "[{}] ({}) {}".format(self.__class__.__name__,
                                       self.id, self.__dict__)
        return string

    def save(self):
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        my_dict = self.__dict__
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()

        return my_dict
