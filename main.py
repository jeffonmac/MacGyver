#! /.envPy3 python3
# -*- coding: utf-8 -*-

import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("img/wallpaper2.png").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage de macgyver
perso = pygame.image.load("img/macgyver-32-43.png").convert_alpha()
fenetre.blit(perso, (5, 43))

# Chargement et collage du guardien
perso = pygame.image.load("img/guard-32.png").convert_alpha()
fenetre.blit(perso, (600, 395))

# Rafraîchissement de l'écran
pygame.display.flip()

# Boucle infinie
continues = True
while continues:
    for event in pygame.event.get():
        if event.type == QUIT:
            continues = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                loop = False
