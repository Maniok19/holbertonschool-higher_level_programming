#!/usr/bin/python3
import pickle


class CustomObject:
    def __init__(self, name: str, age: int, is_student: bool):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (IOError, pickle.PickleError) as e:
            print(f"Serialization error: {e}")
            return None

    @classmethod 
    def deserialize(cls, filename):
        try:
            with open(filename, "rb") as f:
                return pickle.load(f)

        except (IOError, pickle.PickleError) as e:
            print(f"Deserialization error: {e}")
            return None