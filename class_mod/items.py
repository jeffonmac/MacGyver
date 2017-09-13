import random

from constants import *
from class_mod.level import *


class Items:  # the class for the items
    def __init__(self, img_object, level):
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.level = level
        self.loaded = True
        self.img_object = img_object

    def display(self, img_object, window):
        while self.loaded:
            self.case_x = random.randint(0, 5)
            self.case_y = random.randint(0, 5)
            if self.level.structure[self.case_y][self.case_x] == '0':
                self.y = self.case_y * SPRITE_RADING
                self.x = self.case_x * SPRITE_RADING
                self.loaded = False
