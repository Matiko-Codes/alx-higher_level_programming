#!/usr/bin/python3
"""Rectangle module"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry


class Rectangle(BaseGeometry):
    """Class Rectangle that inherits from BaseGeometry (7-base_geometry.py)
    (task based on 8-rectangle.py)"""

    def __init__(self, width, height):
        """Constructor method for Rectangle
        Instantiation with width and height"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """Return area of rectangle"""

        area = self.__width * self.__height
        return area

    def __str__(self):
        """Returns string representation of a Rectangle"""

        string = "[Rectangle] {}/{}".format(self.__width, self.__height)
        return string