#!/usr/bin/python3
"""From the same class or inherits from the class
Author: Matiko

"""


def is_kind_of_class(obj, a_class):
    """ check if an object is an instance of a class
    that inherited from the class"""

    if isinstance(obj, a_class):
        return True
    return False