#!/usr/bin/python3
"""module for base class
"""
import json
import csv


class Base:
    """base class
    private class attribute __nb_objects = 0
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries == [] or list_dictionaries is None:
            return json.dumps([])
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        if json_string is None or json_string == []:
            return json.loads([])
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        filename = cls.__name__ + ".json"
        try:
            with open(filename, "r", encoding="utf-8") as file:
                json_string = file.read()
        except FileNotFoundError:
            return []

        if not json_string:
            return []

        json_list = json.loads(json_string)
        instances = [cls.create(**data) for data in json_list]
        return instances

    @classmethod
    def save_to_file_csv(cls, list_objs):
        filename = cls.__name__ + ".csv"

        with open(filename, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)

            if list_objs is not None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    attributes = ["id", "width", "height", "x", "y"]
                else:
                    attributes = ["id", "size", "x", "y"]

                writer = csv.DicWriter(csv_file, fieldnames=attributes)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        filename = cls.__name__ + ".csv"
        instances = []

        try:
            with open(filename, "r") as textfile:
                json_string = textfile.read()
                instance_dicts = cls.from_json_string(json_string)

                for instance_dict in instance_dicts:
                    instances.append(cls.create(**instance_dict))
        except FileNotFoundError:
            pass

        return instances

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise NotImplementedError
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def save_to_file(cls, list_objs):
        if list_objs is None:
            data = "[]"
        else:
            data = cls.to_json_string([obj.to_dictionary()
                                       for obj in list_objs])
        file = cls.__name__ + ".json"
        with open(file, mode='w', encoding="utf-8") as f:
            f.write(data)
