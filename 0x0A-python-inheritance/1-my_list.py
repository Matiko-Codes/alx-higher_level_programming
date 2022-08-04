#!/usr/bin/python3
"""My list
Author: Matiko"""


class MyList(list):
    """A class MyList that inherits from list"""

    def print_sorted(self):
        """Prints the list in a sorted ascending order"""
        print(sorted(self))