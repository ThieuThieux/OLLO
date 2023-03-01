import pygame
from pygame.locals import *

pygame.init()
offsetX = 80
centre = (317-22+80,238-22)

fenetre = pygame.display.set_mode((640,480))

idle_on = 1

fond = pygame.image.load(r"img\fond3-4.png").convert()

fenetre.blit(fond,(0,0))

bille = pygame.image.load(r"img\bille_bleu.png").convert_alpha()
fenetre.blit(bille, centre)
pygame.display.flip()

while idle_on:
    idle_on = int(input())

