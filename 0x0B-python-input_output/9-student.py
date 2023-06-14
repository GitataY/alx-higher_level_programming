#!/usr/bin/python3
""" this module is vlass to json"""


class Student:
    """Class representing a student"""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student instance"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieve a dictionary rep of a Student instance"""
        return {
            'first_name': self.first_name,
            'last_name': self.last_name,
            'age': self.age
        }