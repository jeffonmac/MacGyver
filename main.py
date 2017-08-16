#! /.envPy3 python3
# coding: utf-8

import pygame
from pygame.locals import *

pygame.init()

# Ouverture de la fenêtre Pygame
fenetre = pygame.display.set_mode((640, 480))

# Chargement et collage du fond
fond = pygame.image.load("/img/wallpaper.png").convert()
fenetre.blit(fond, (0, 0))

# Chargement et collage du personnage
perso = pygame.image.load("/img/macgyver-32-43.png").convert_alpha()
fenetre.blit(perso, (32, 43))

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
