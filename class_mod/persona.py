#! /.envPy3 python3
# -*- coding: utf-8 -*-

"""

MacGyver Labyrinth Game Class

"""

import pygame

from constants import *


class Persona:
    """ Class to create a character """

    def __init__(self, right, left, up, low, level):
        # Sprites of the character
        self.right = pygame.image.load(right).convert_alpha()
        self.left = pygame.image.load(left).convert_alpha()
        self.up = pygame.image.load(up).convert_alpha()
        self.low = pygame.image.load(low).convert_alpha()
        # Position of the character in boxes and in pixels
        self.case_x = 0
        self.case_y = 0
        self.x = 0
        self.y = 0
        # Default direction
        self.direction = self.right
        # Level in which the character is located
        self.level = level

    def move(self, direction):
        """ A method for moving the character """

        if direction == 'right':
            # Not to exceed the screen
            if self.case_x < (num_sprite_rating - 1):
                # Check that the destination box is not a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # Moving +1
                    self.case_x += 1
                    # The "real" pixel position
                    self.x = self.case_x * sprite_rating
            # Image in the right direction
            self.direction = self.right

        # Moving to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * sprite_rating
            self.direction = self.left

        # Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * sprite_rating
            self.direction = self.up

        # Moving Down
        if direction == 'down':
            if self.case_y < (num_sprite_rating - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * sprite_rating
            self.direction = self.low
