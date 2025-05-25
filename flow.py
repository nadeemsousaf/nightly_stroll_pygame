import pygame
from sys import exit
from obj_class import *
from state import *
from npc import *

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Nightly Stroll')
clock = pygame.time.Clock()

game_state = 0 #keeps track of game location
player = Player(0,0,0)

while True:
    if game_state == 0:
        print("do this")
    elif game_state == 1:
        print("do that")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                player.y_dir = 1
                player.show = player.front
            elif event.key == pygame.K_UP:
                player.y_dir = -1
            elif event.key == pygame.K_LEFT:
                player.x_dir = -1
                player.show = player.left
            elif event.key == pygame.K_RIGHT:
                player.x_dir = 1
                player.show = player.right
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                player.y_dir = 0
            elif event.key == pygame.K_UP:
                player.y_dir = 0
            elif event.key == pygame.K_LEFT:
                player.x_dir = 0
            elif event.key == pygame.K_RIGHT:
                player.x_dir = 0

    window.blit(npc1.normal_img, (npc1.x,npc1.y)) #test works, image appears
    pygame.display.update()
    clock.tick(40)