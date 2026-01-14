#pygame image loader- not yet using, images currently created in npc.py
#pass all in structure thru convert alpha func after display made in flow.py?
import pygame

all_images = {} #use this



game_buttons_img = [pygame.image.load('game_images/startBN.jpg'),pygame.image.load('game_images/startBA.jpg'),pygame.image.load('game_images/restartBN.jpg'),pygame.image.load('game_images/restartBA.jpg'),pygame.image.load('game_images/resumeBN.jpg'),pygame.image.load('game_images/resumeBA.jpg'),pygame.image.load('game_images/quitBN.jpg'),pygame.image.load('game_images/quitBA.jpg')]
for i in range(len(game_buttons_img)):
    game_buttons_img[i] = pygame.transform.scale(game_buttons_img[i], (100,50))

great_wave = pygame.image.load('game_images/great_wave.jpg')
title_test = pygame.image.load('game_images/title_test.png')
are_you_sure = pygame.image.load('game_images/are_you_sure.jpg')
my_guy1 = pygame.transform.scale(pygame.image.load('game_images/my_guy1.png'),(200,200))
my_guy2 = pygame.transform.scale(pygame.image.load('game_images/my_guy2.png'),(200,200))
my_guy3 = pygame.transform.scale(pygame.image.load('game_images/my_guy3.png'),(200,200))
my_guy4 = pygame.transform.scale(pygame.image.load('game_images/my_guy4.png'),(200,200))
my_guy5 = pygame.transform.scale(pygame.image.load('game_images/my_guy5.png'),(200,200))
my_guy6 = pygame.transform.scale(pygame.image.load('game_images/my_guy6.png'),(200,200))
quit_b = pygame.transform.scale(pygame.image.load('game_images/quit_b.png'),(150,70)) #
quit_ba = pygame.transform.scale(pygame.image.load('game_images/quit_ba.png'),(150,70)) #
player1 = pygame.image.load('game_images/player1.png')
player2 = pygame.image.load('game_images/player2.png')
player3 = pygame.image.load('game_images/player3.png')

resize_test = [my_guy1,my_guy2,my_guy3,my_guy4,my_guy5,my_guy6]
