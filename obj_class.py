import pygame
from button_functions import *

class CustSprite():
    def __init__(self,x,y,normal_img):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,normal_img.get_width(),normal_img.get_height()) #height goes positive downward...?, width & height catered to normal state
        self.normal_img = normal_img
        self.show_img = normal_img

    def get_top_left(self):
        return self.rect.topleft
    
    def get_top_right(self):
        return self.rect.topright
    
    def get_bottom_left(self):
        return self.rect.bottomleft
    
    def get_bottom_right(self):
        return self.rect.bottomright
    
    def draw(self,game_window):
        game_window.blit(self.show_img,(self.x,self.y))

    def update(self,event):
        pass

class Player(CustSprite):
    def __init__(self,x,y,front_img1,front_img2,left_img1,left_img2,right_img1,right_img2):
        super().__init__(x,y,front_img1)
        self.front_img1 = front_img1
        self.front_img2 = front_img2
        self.left_img1 = left_img1
        self.left_img2 = left_img2
        self.right_img1 = right_img1
        self.right_img2 = right_img2
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
        self.health = 200
        self.pause = False
    
    def set_forward(self):
        if self.show_img == self.front_img1:
            self.show_img = self.front_img2
        else:
            self.show_img = self.front_img1

    def set_left(self):
        if self.show_img == self.left_img1:
            self.show_img = self.left_img2
        else:
            self.show_img = self.left_img1

    def set_right(self):
        if self.show_img == self.right_img1:
            self.show_img = self.right_img2
        else:
            self.show_img = self.right_img1
    
    def set_x_dir(self,x):
        self.x_dir = x
    
    def set_y_dir(self,y):
        self.x_dir = y

    def walk(self):
        if self.pause != True:
            self.x += self.speed*self.x_dir
        
    def pause_player(self):
        self.pause = True

    def unpause_player(self):
        self.pause = False

    def set_xy(self,coord_tuple): #expects a tuple of len 2 with x,y
        if coord_tuple[0] != None:
            self.x = coord_tuple[0]
        if coord_tuple[1] != None:
            self.y = coord_tuple[1]
        

class NPC(CustSprite):
    def __init__(self,x,y,front_img,left_img,right_img):
        super().__init__(x,y,front_img)
        self.front_img = front_img
        self.left_img = left_img
        self.right_img = right_img

    def motion(self):
        pass

class TextBubble(CustSprite): #separate text from text box? Or one image?
    def __init__(self,text,x,y,txt_x,txt_y,font,normal_img,colour):
        super().__init__(x,y,normal_img)
        self.txt_obj = font.render(text,False,colour) #text object to go over text bubble
        self.txt_x = txt_x
        self.txt_y = txt_y

    def draw(self,game_window):
        super().draw(game_window)
        game_window.blit(self.txt_obj, (self.txt_x,self.txt_y))

class Button(CustSprite):
    def __init__(self,x,y,normal_img,hover_img,action=None): #only need 2 images for button
        super().__init__(x,y,normal_img)
        self.hover_img = hover_img
        self.action = action

    def draw(self,game_window):
        super().draw(game_window)

    def set_click_response(self,action):
        self.action = action #lambda

    def update(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos): #mouse hovering
            self.show_img = self.hover_img
            if event.type == pygame.MOUSEBUTTONDOWN: #button clicked
                self.show_img = self.normal_img
                #print("click")
                if self.action != None:
                    return self.action()
        else:
           self.show_img = self.normal_img 
           return None

class NodeT(): #for tree with no built-in reversal (storyline/map)
    def __init__(self,data):
        self.data = data #StateWalk or StateTalk
        self.l = None
        self.r = None
        self.f = None

    def set_left(self,l):
        self.l = l

    def set_right(self,r):
        self.r = r

    def set_forward(self,f):
        self.f = f

class State(): #sub-classes for walking vs talking?
    def __init__(self,number,events,sprites,bg,mg=None,fg=None):
        self.number = number
        self.bg = bg
        self.mg = mg
        self.fg = fg
        self.events = events
        self.sprites = sprites

    def draw(self,game_window):
        game_window.blit(self.bg,(0,0)) #update custom x & y
        if self.mg != None:
            game_window.blit(self.mg,(0,0)) #update custom x & y
        if self.fg != None:
            game_window.blit(self.fg,(0,0)) #update custom x & y
        for x in self.sprites:
            x.draw(game_window)

    def update(self,event):
        for x in self.sprites:
            re = x.update(event)
            if re != None:
                return re

class StateWalk(State):
    '''
    def __init__(self,number,bg,mg,fg,events,sprites):
        super().__init__(self,number,bg,mg,fg,events,sprites)
    '''
    def walk(self):
        self.sprites[0].walk() #player must always come first in list of sprites

    def update(self,event):
        for x in self.sprites:
            self.walk()
            re = x.update(event)
            if re != None:
                return re
        #if player.x is past certain threshold- next state? change image?

    def get_player(self):
        return self.sprites[0]

class StateTalk(State):
    def test(self):
        pass

