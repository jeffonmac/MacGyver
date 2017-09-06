#! /.envPy3 python3
# -*- coding: utf-8 -*-

"""

MacGyver Labyrinth Game Class

"""
import pygame
import constants

"""

Method for generating the level based on the file.
       We create a general list, containing a list per line to be displaye
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
        wall = pygame.image.load(constants.image_wall).convert()
        starting = pygame.image.load(constants.image_start).convert()
        arrival = pygame.image.load(constants.image_arrival).convert_alpha()

        # The list of levels
        num_line = 0
        for line in self.structure:
            # The list of lines
            num_case = 0
            for sprite in line:
                # Calculates the actual pixel position
                x = num_case * constants.sprite_rating
                y = num_line * constants.sprite_rating
                if sprite == 'm':  # m = Wall
                    window.blit(wall, (x, y))
                elif sprite == 'd':  # d = Start
                    window.blit(starting, (x, y))
                elif sprite == 'a':  # a = Arrival
                    window.blit(arrival, (x, y))
                num_case += 1
            num_line += 1


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
            if self.case_x < (constants.num_sprite_rating - 1):
                # Check that the destination box is not a wall
                if self.level.structure[self.case_y][self.case_x + 1] != 'm':
                    # Moving +1
                    self.case_x += 1
                    # The "real" pixel position
                    self.x = self.case_x * constants.sprite_rating
            # Image in the right direction
            self.direction = self.right

        # Moving to the left
        if direction == 'left':
            if self.case_x > 0:
                if self.level.structure[self.case_y][self.case_x - 1] != 'm':
                    self.case_x -= 1
                    self.x = self.case_x * constants.sprite_rating
            self.direction = self.left

        # Move up
        if direction == 'up':
            if self.case_y > 0:
                if self.level.structure[self.case_y - 1][self.case_x] != 'm':
                    self.case_y -= 1
                    self.y = self.case_y * constants.sprite_rating
            self.direction = self.up

        # Moving Down
        if direction == 'down':
            if self.case_y < (constants.num_sprite_rating - 1):
                if self.level.structure[self.case_y + 1][self.case_x] != 'm':
                    self.case_y += 1
                    self.y = self.case_y * constants.sprite_rating
            self.direction = self.low
