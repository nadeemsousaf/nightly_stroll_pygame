#pygame image loader- not yet using, images currently created in npc.py
#isometric?
import pygame
test = pygame.image.load('game_images/test.png')

startBN = pygame.image.load('game_images/startBN.jpg')
startBN_img = pygame.transform.scale(startBN, (100,50))
startBA = pygame.image.load('game_images/startBA.jpg')
startBA_img = pygame.transform.scale(startBA, (100,50))

restartBN = pygame.image.load('game_images/restartBN.jpg')
restartBA = pygame.image.load('game_images/restartBA.jpg')
resumeBN = pygame.image.load('game_images/resumeBN.jpg')
resumeBA = pygame.image.load('game_images/resumeBA.jpg')
quitBN = pygame.image.load('game_images/quitBN.jpg')
quitBA = pygame.image.load('game_images/quitBA.jpg')

great_wave = pygame.image.load('game_images/great_wave.jpg')
