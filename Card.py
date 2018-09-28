"""
Name: Card.py
Author:
Init Date: 28 September, 2018

Latest Edit: 28 September, 2018
Edited by: David Gurevich

Finally worked: 28, September, 2018
Time: 9:5

{Documentation goes here}
"""

import pygame

class Card(object):
    def __init__(self, col, row, id):
        self._col = col
        self._row = row

        self._id = id

    def draw(self, screen):
        pass
        
    # Getters and Setters example
    def get_col(self):
        return self._col

    def set_col(self, col):
        self._col = col

    def get_row(self):
        return self._row

    def set_row(self):
        self._row = row

    
