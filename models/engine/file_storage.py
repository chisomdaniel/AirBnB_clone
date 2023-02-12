#!/usr/bin/python3
'''This module contain the `FileStorage` class that
serializes instances to JSON fileand deserializes
JSON file to instances
'''
import json
from models.base_model import BaseModel


class FileStorage:
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        string = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[string] = obj

    def save(self):
        new_dict = {}
        for key, value in self.__objects.items():
            new_dict[key] = value.to_dict()

        with open(self.__file_path, 'w') as fd:
            json.dump(new_dict, fd)

    def reload(self):

        try:
            with open(self.__file_path, 'r') as fd:
                self.__objects = json.load(fd)

            for key, value in self.__objects.items():
                class_name = key.split('.')[0]
                self.__objects[key] = eval(class_name)(**value)

        except FileNotFoundError:
            return
