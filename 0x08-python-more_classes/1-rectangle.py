#!/usr/bin/python3
"""
Module 2-rectangle
Contains class Rectangle
with private attribute width and height
"""


class Rectangle:
    """
    Defines class rectangle with private attribute width and height

    Args:
    width (int): width
    height (int): height

    Functions:
    __init__(self, width=0, height=0):
    width(self)
    width(self, value)
    height(self)
    height(self, value)
    """
    def __init__(self, width=0, height=0):
        """ Initializes rectangles """
        self.width = width
        self.height = height

        @proper
