import pygame

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
        placeholder = "placeholder"

class Player(CustSprite):
    def __init__(self,front_img,left_img,right_img):
        super().__init__(0,245,front_img)
        self.front_img = front_img
        self.left_img = left_img
        self.right_img = right_img
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
        self.health = 200

class NPC(CustSprite):
    def __init__(self,x,y,front_img,left_img,right_img):
        super().__init__(x,y,front_img)
        self.front_img = front_img
        self.left_img = left_img
        self.right_img = right_img
    def motion(self):
        print("placeholder")

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
    def __init__(self,x,y,normal_img,hover_img): #only need 2 images for button
        super().__init__(x,y,normal_img)
        self.hover_img = hover_img
        self.action = None
        self.state = None
    def draw(self,game_window):
        super().draw(game_window)
    def set_click_response(self,state,action):
        self.state = state
        self.action = action
    def update(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos): #mouse hovering
            self.show_img = self.hover_img
            if event.type == pygame.MOUSEBUTTONDOWN: #button clicked
                self.show_img = self.normal_img #sleep to show clicked button?
                #print("click")
                if self.state != None:
                    self.state.update() #load next state
                #return self.direction
        else:
           self.show_img = self.normal_img 

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
    def __init__(self,number,bg,mg,fg,events,sprites):
        self.number = number
        self.bg = bg
        self.mg = mg
        self.fg = fg
        self.events = events
        self.sprites = sprites
        #self.state = events.data #singly-linked list...?
        self.exit = False
    def draw(self,game_window):
        game_window.blit(self.bg,(0,0)) #update custom x & y
        game_window.blit(self.mg,(0,0)) #update custom x & y
        game_window.blit(self.fg,(0,0)) #update custom x & y
        for x in self.sprites:
            x.draw(game_window)
    def update(self,event):
        for x in self.sprites:
            x.update(event)
    def open_exit(self): #change to accomodate for direction
        self.exit = True #triggers an event, moves to next scene, more code to come

class StateWalk(State):
    def __init__(self,number,bg,mg,fg,events,sprites):
        super().__init__(self,number,bg,mg,fg,events,sprites)
    def walk(self,player):
        for event in pygame.event.get():
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
    def update(self):
        self.walk()
        #if player.x is past certain threshold- next state? change image?

class StateTalk(State):
    def __init__(self,number,bg,mg,fg,events,sprites):
        super().__init__(self,number,bg,mg,fg,events,sprites) 

