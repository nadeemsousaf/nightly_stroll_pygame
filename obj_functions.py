import pygame

def resize_for_win_logic(img,win_tuple):
    return pygame.transform.scale(img,(img.get_width()*(win_tuple[1][0]/win_tuple[0][0]),img.get_height()*(win_tuple[1][1]/win_tuple[0][1])))