#pygame image loader- not yet using, images currently created in npc.py
#isometric?
import pygame
test = pygame.image.load('game_images/test.png')

game_buttons_img = [pygame.image.load('game_images/startBN.jpg'),pygame.image.load('game_images/startBA.jpg'),pygame.image.load('game_images/restartBN.jpg'),pygame.image.load('game_images/restartBA.jpg'),pygame.image.load('game_images/resumeBN.jpg'),pygame.image.load('game_images/resumeBA.jpg'),pygame.image.load('game_images/quitBN.jpg'),pygame.image.load('game_images/quitBA.jpg')]
for i in range(len(game_buttons_img)):
    game_buttons_img[i] = pygame.transform.scale(game_buttons_img[i], (100,50))

great_wave = pygame.image.load('game_images/great_wave.jpg')
