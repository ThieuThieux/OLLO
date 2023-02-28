import pygame
from pygame.locals import *

pygame.init()

fenetre = pygame.display.set_mode((640,480))

idle_on = 1

fond = pygame.image.load(r"img\background.jpg").convert()

fenetre.blit(fond,(0,0))

pygame.display.flip()

while idle_on:
    idle_on = int(input())

