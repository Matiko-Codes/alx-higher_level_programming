#!/usr/bin/python3
"""Exact same object
Author: Matiko

"""


def is_same_class(obj, a_class):
    """ Check is object is instance of the class"""

    if type(obj) == a_class:
        return True
    return False