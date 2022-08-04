#!/usr/bin/python3
"""Class BaseGeometry
Author: Matiko

"""


class BaseGeometry:
    """An empty class"""

    def area(self):
        """Raises an exception because area is not implimented"""
        
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value"""

        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))