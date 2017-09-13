#! /.envPy3 python3
# -*- coding: utf-8 -*-

from pygame.locals import *

# from class_mod.items import Items  # in test #
from class_mod.items import *
from class_mod.level import *
from class_mod.persona import *
from constants import *



class Game:
    def mainloop(self):
        pygame.init()
        # Opening the Pygame window
        window = pygame.display.set_mode((SIDE_WINDOW, SIDE_WINDOW))
        # Title
        pygame.display.set_caption(WINDOW_TITLE)

        # Variables to check if the items have been picked or not:
        Treasure_one = True
        Treasure_two = True
        Treasure_three = True
        win = False

        level = Level('n1')
        tresorImg = pygame.image.load(TREASURE).convert_alpha()
        treas = Items(tresorImg, level)
        treas.display(tresorImg, window)

        # Main Loop
        go_on = 1
        while go_on:
            # Display of the home screen
            welcome = pygame.image.load(IMAGE_HOME).convert()
            window.blit(welcome, (0, 0))
            # Refresh
            pygame.display.flip()
            # These variables are set to 1 at each loop turn
            continue_game = True
            continue_welcome = True
            # Welcome loop
            while continue_welcome:
                # Loop speed limit
                pygame.time.Clock().tick(25)
                for event in pygame.event.get():
                    # If the user exits, the variables
                    # Loop to False to go through none and close
                    if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                        continue_welcome = False
                        continue_game = False
                        go_on = False
                        # Variable of choice of level
                        choice = 0
                    elif event.type == KEYDOWN:
                        # Launch of Level
                        if event.key == K_F1:
                            continue_welcome = False  # We leave the reception
                            choice = 'n1'  # Set the level to be loaded

            # Not to load if it leaves
            if choice != 0:
                # Loading the background
                wall = pygame.image.load(IMAGE_BACKGROUD).convert()
                # Generating a level from a file
                level = Level(choice)
                level.generate()
                level.display(window)
                # Creating MacGyver
                macg = Persona("img/macgyver.png", "img/macgyver_2.png", "img/macgyver_3.png", "img/macgyver_4.png",
                               level)
            # Game loop
            while continue_game is True:
                # Loop speed limit
                pygame.time.Clock().tick(25)
                for event in pygame.event.get():
                    # If the user exits, set the variable that continues the game
                    # and the general variable to False to close the window
                    if event.type == QUIT:
                        continue_game = False
                        go_on = False
                    elif event.type == KEYDOWN:
                        # If the user presses Esc here, we only return to the menu
                        if event.key == K_ESCAPE:
                            continue_game = False
                        # MacGyver move keys
                        elif event.key == K_RIGHT:
                            macg.move('right')
                        elif event.key == K_LEFT:
                            macg.move('left')
                        elif event.key == K_UP:
                            macg.move('up')
                        elif event.key == K_DOWN:
                            macg.move('down')
                # Views to new positions
                window.blit(wall, (0, 0))
                level.display(window)
                # macg.direction = the image in the right direction
                window.blit(macg.direction, (macg.x, macg.y))
                pygame.display.flip()
                # Victory -> Back to Home
                if level.structure[macg.case_y][macg.case_x] == 'a':
                    continue_game = False

                    if Treasure_one:
                        window.blit(treas.img_object, (treas.x, treas.y))
                    if (macg.x, macg.y) == (treas.x, treas.y):
                        Treasure_one = False
                        window.blit(treas.img_object, (0, 0))

                    if Treasure_three:
                        window.blit(treas.img_object, (treas.x, treas.y))
                    if (macg.x, macg.y) == (treas.x, treas.y):
                        Treasure_three = False
                        window.blit(treas.img_object, (10, 0))

                    if Treasure_two:
                        window.blit(treas.img_object, (treas.x, treas.y))
                    if (macg.x, macg.y) == (treas.x, treas.y):
                        Treasure_two = False
                        window.blit(treas.img_object, (30, 0))

                    # refreshing screen
                    pygame.display.flip()

                    # EndGame Victory or loose
                    if level.structure[macg.case_y][
                        macg.case_x] == 'a':  # If MacGyver reach the guard he win and the game is terminated.
                        if Treasure_one == False:
                            if Treasure_three == False:
                                if Treasure_two == False:
                                    win = True

                    if win == True:
                        window.blit(wall, (0, 0))
                        font = pygame.font.Font(None, 25)
                        text = font.render("You win !", 1, (255, 255, 255))
                        textrect = text.get_rect()
                        textrect.centerx, textrect.centery = SPRITE_RADING / 2, SPRITE_RADING / 2
                        window.blit(text, textrect)
