#!/usr/bin/python3
"""This Imports some standard modules and modules from the project packages"""
import json
from models.base_model import BaseModel
from datetime import datetime as dt 

"""
This is the Python class that will be responsible for the file storage.
"""


class FileStorage():
    """
    This is the class responsible for data storage for AirBnB Clone project.
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self) -> dict:
        return self.__objects

    def new(self, obj: dict) -> None:
    """
    This is the public instance of the method that sets in `__objects` `obj` with
    the key
    Args:
     obj (dict) - the dictionaary object of the file
    """
    fmt = "{}.{}".format(obj.__class__.__name__, obj.id)
    self.__objects[fmt] = obj

    def save(self) -> None:
    """
    This is a public instance method that serializes the private instance
    object `__objects` (dict) into a JSON string and save it to a flat
    database (json file)
    """
    dict_serial = {}
    with open(self.__file_path, mode="w", encoding="utf-8") as fn:
        for key, val in self.__objects.items():
            dict_serial[key] = val.to_dict()
        json.dump(dict_serial, fn)

    def reload(self) -> None:
    """
    This is the public instance of the method that deserializes the json string into
    a dictionary object `__objects` only if the  `__file_path` exist.
    """
    try:
        with open(self.__file_path, mode="r", encoding="utf-8") as fn:
            data_strm = json.load(fn)
        for key, val in data_strm.items():
            class_name = key.split(".")[0]
            self.new(eval(class_name + "(**val)"))
    except:
        ...
