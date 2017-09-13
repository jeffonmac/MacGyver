import random

from constants import *


class Items:  # the class for the items
    def __init__(self, img_object, elv):
        self.case_y = 0
        self.case_x = 0
        self.x = 0
        self.y = 0
        self.elv = elv
        self.loaded = True
        self.img_object = img_object

    def display(self):
        while self.loaded:
            self.case_x = random.randint(0, 14)
            self.case_y = random.randint(0, 14)
            if self.elv.structure[self.case_y][
                self.case_x] == '0':  # l'inversement de self.case_x, self.case_y permet de faire ce que je veux !!! (l'inverse fais apparaitre les objets dans les murs. Youpi !)
                self.y = self.case_y * SPRITE_RADING
                self.x = self.case_x * SPRITE_RADING
                self.loaded = False
