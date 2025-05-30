import pygame

#need to determine ownership of each event: when NPC moves in a scene, do these moves belong to the NPC or the State object?

class CustSprite(): #add draw function? window doesn't exist yet...
    def __init__(self,x,y,normal_img):
        self.x = x
        self.y = y
        self.rect = pygame.Rect(x,y,x+normal_img.get_width(),y+normal_img.get_height()) #height goes positive downward...?, width & height catered to normal state
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
        game_window.blit(self.normal_img,(self.x,self.y))

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

class Motion(): #if npc moves and/or speaks
    def __init__(self,dialogue,movement):
        self.dialogue = dialogue
        self.movement = movement

class NPC(CustSprite):
    def __init__(self,x,y,front_img,left_img,right_img,events):
        super().__init__(x,y,front_img)
        self.x = x
        self.y = y
        self.front_img = front_img
        self.left_img = left_img
        self.right_img = right_img
        self.events = events #singly-linked list of action(s)
        self.health = 100 #maybe necessary
        self.trigger = False #to trigger a motion
    def motion(self): #speak and/or move during user interaction
        print("placeholder")

class TextBubble(CustSprite): #unsure if will require images
    def __init__(self,text,x,y,txt_x,txt_y,font,normal_img,colour):
        super().__init__(x,y,normal_img)
        self.txt_obj = font.render(text,False,colour) #text object to go over text bubble
        self.txt_x = txt_x
        self.txt_y = txt_y
    def draw(self,game_window):
        super().draw(self,game_window)
        game_window.blit(self.txt_obj, (self.txt_x,self.txt_y))

class Button(TextBubble):
    def __init__(self,text,x,y,txt_x,txt_y,font,normal_img,colour,hover_img,click_img):
        super().__init__(text,x,y,txt_x,txt_y,font,normal_img,colour)
        self.click_img = click_img
        self.hover_img = hover_img
        self.click = False
        self.hover = False
    def hover(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.hover = True
            self.show_img = self.hover_img
        else: #check if else if necessary
            self.hover = False
            self.show_img = self.normal_img
    def click(self):
         for event in pygame.event.get():
            if event.type ==pygame.MOUSEBUTTONDOWN:
                if self.hover == True:
                    self.show_img = self.click_img
                    self.click = True #triggers an event, more code to come

class NodeL(): #for singly-linked list (events by scene & npc actions)
    def __init__(self,data):
        self.data = data
        self.next = None
    def set_next(self,next):
        self.next = next

class NodeT(): #for tree with no built-in reversal (storyline/map)
    def __init__(self,data):
        self.data = data
        self.l = None
        self.r = None
        self.f = None
    def set_left(self,l):
        self.l = l
    def set_right(self,r):
        self.r = r
    def set_forward(self,f):
        self.f = f

class State(): #requires list of objects to render on scene? (on top of fg,mg,bg images)- sprite? no...
    def __init__(self,number,bg,mg,fg,exit_x,current):
        self.number = number
        self.bg = bg
        self.mg = mg
        self.fg = fg
        self.exit_x = exit_x
        self.current = current #singly-linked list of events
        self.exit = False
    def draw(self):
        print("placeholder")
    def open_exit(self):
        self.exit = True