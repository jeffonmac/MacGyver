#! /.envPy3 python3
# -*- coding: utf-8 -*-

"""

MacGyver Labyrinth Game Class

"""

import pygame
# from random import randint

from constants import *


class Level:
    """ Class to create a level """

    def __init__(self, file):
        self.files = file
        self.structure = [0]

    def generate(self):

        """

        Method for generating the level based on the file.
         We create a general list, containing a list per line to be displayed

        """

        # Open file :
        with open(self.files, "r") as file:
            structure_level = []
            # Runs through the lines of the file
            for line in file:
                line_level = []
                # The sprites (letters) contained in the file
                for sprite in line:
                    # We ignore the "\ n" of end of line
                    if sprite != '\n':
                        # Add the sprite to the list of the line
                        line_level.append(sprite)
                # Adds the line to the level list
                structure_level.append(line_level)
            # Saving
            self.structure = structure_level

    def display(self, window):

        """

        Method for displaying the level in function
         Of the structure list returned by generer ()

        """

        # Loading images
        wall = pygame.image.load(IMAGE_WALL).convert()
        starting = pygame.image.load(IMAGE_START).convert()
        arrival = pygame.image.load(IMAGE_ARRIVAL).convert_alpha()
        treasure_r = pygame.image.load(TREASURE).convert_alpha()

        # The list of levels
        num_line = 0
        # z = randint(1, 2)
        for line in self.structure:
            # The list of lines
            num_case = 0
            for sprite in line:
                # Calculates the actual pixel position
                x = num_case * SPRITE_RADING
                y = num_line * SPRITE_RADING
                if sprite == 'm':  # m = Wall
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Start
                    window.blit(starting, (x, y))
                elif sprite == 'a':  # a = Arrival
                    window.blit(arrival, (x, y))
                elif sprite == 'z':
                    window.blit(treasure_r, (x, y))
                num_case += 1
            num_line += 1
