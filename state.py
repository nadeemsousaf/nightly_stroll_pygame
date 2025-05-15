import pygame
from sys import exit
import random

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Nightly Stroll')
clock = pygame.time.Clock()

game_state = 0 #keeps track of game location