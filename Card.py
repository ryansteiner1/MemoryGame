"""
Name: Card.py
Author:
Init Date: 28 September, 2018

Latest Edit: 1 October, 2018
Edited by: Ryan Steiner

{Documentation goes here}
"""

import pygame

class Card(object):
    def __init__(self, col, row, num, active, flipped):
        self._cord = (col, row)
        self._num = num
        self._image = pygame.image.load("assets/%s") % str(self._num)
        self._cardback = pygame.image.load("assets/Card.png")
        self._flipped = False
        self._active = True

    def restart(self):
        self._flipped = False
        self._actve = True
    
    def draw(self, screen):
        if self._flipped:
            screen.blit(self._image,(self.col,self._row))
        else:
            screen.blit(self._cardback,(self._col,self._row))
            
    def get_cord(self):
        return self._cord

    def set_cord(self,cord):
        self._cord = cord

    def get_num(self):
        return self._num

    def set_num(self):
        self._num = num

    def get_flipped(self):
        return self._flipped

    def set_flipped(self,flipped):
        self._flipped = fipped

    def get_active(self):
        return self._active

    def set_active(self,active):
        self._active = active

    def __eq__(self,other):
        if self.get_num == other.get_num:
            return True
        else:
            return False
