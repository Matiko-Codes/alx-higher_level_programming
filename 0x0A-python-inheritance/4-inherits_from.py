#!/usr/bin/python3
"""Only sub class of
Author: Matiko

"""


def inherits_from(obj, a_class):
"""object is an instance of a class that inherited (directly or indirectly) from the specified class
"""
    if issubclass(type(obj), a_class) and type(obj) is not a_class:
        return True
    return False