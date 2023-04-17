#!/usr/bin/python3
"""Creation of a class Base"""
import json
import os


class Base:
    """definition of the attributs and methods of the class"""

    __nb_objects = 0

    def __init__(self, id=None):
        """instanziation of a base class
        Args:
            id (int): id of the instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        Args:
            list_dictionaries (list): list of dictio
        """
        res = []
        if list_dictionaries is not None:
            if type(list_dictionaries) is not list:
                ms = "list_dictionaries must be a list of dictionaries"
                raise TypeError(ms)
            if len(list_dictionaries) > 0:
                for dic in list_dictionaries:
                    if type(dic) is not dict:
                        ms = "list_dictionaries must be a list of dictionaries"
                        raise TypeError(ms)
                res = json.dumps(list_dictionaries)
        return res

    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of
        list_objs to a file
        Args:
            cls (): cls
            list_objs (list): list of instance
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, mode="w") as myFile:
            if list_objs is None:
                myFile.write("[]")
            else:
                ins = [ob.to_dictionary() for ob in list_objs]
                myFile.write(Base.to_json_string(ins))

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON string
        representation json_string
        Args:
            json_string (str): json string
        """
        res = []
        if json_string is not None:
            res = json.loads(json_string)
        return res

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        Args:
            cls : cls
            dictionary (dict): dictionary
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        elif cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        result = []
        listDict = []
        myFile = cls.__name__ + ".json"

        if os.path.exists(myFile):
            with open(myFile, 'r') as f:
                re = f.read()
                listDict = cls.from_json_string(re)
                for di in listDict:
                    result.append(cls.create(**di))
        return result
