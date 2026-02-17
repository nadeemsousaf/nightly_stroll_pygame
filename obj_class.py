from obj_functions import *

class CustSprite():
    def __init__(self,x,y,normal_img):
        self.x = x #necessary?
        self.y = y #necessary?
        self.rect = pygame.Rect(x,y,normal_img.get_width(),normal_img.get_height()) #don't need rect accurate for each img, just overall representation
        self.normal_img = normal_img
        self.show_img = normal_img
    
    def draw(self,game_window):
        game_window.blit(self.show_img,(self.x,self.y))

    def update(self,event):
        pass
    
    def resize_for_win(self,win_tuple):
        new_dim = resize_dim(self.show_img,win_tuple)
        self.rect = pygame.Rect(self.x,self.y,new_dim[0],new_dim[1])
        self.normal_img = resize_for_win_logic(self.normal_img,win_tuple)
        self.show_img = resize_for_win_logic(self.show_img,win_tuple)

    def get_obj_rect(self):
        return self.rect
    
class Critter(CustSprite):
    def __init__(self,x,y,front_img,left_img,right_img):
        super().__init__(x,y,front_img[0])
        self.front_img1 = front_img[0]
        self.front_img2 = front_img[1]
        self.left_img1 = left_img[0]
        self.left_img2 = left_img[1]
        self.right_img1 = right_img[0]
        self.right_img2 = right_img[1]
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
        self.health = 200
        self.pause = False
        self.img_counter = 0
    
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

    def set_xy(self,coord_tuple): #expects a tuple of len 2 with x,y
        if coord_tuple[0] != None:
            self.x = coord_tuple[0]
        if coord_tuple[1] != None:
            self.y = coord_tuple[1]
        self.rect = pygame.Rect(self.x,self.y,self.normal_img.get_width(),self.normal_img.get_height()) 

class Player(Critter):
    def update(self,event): #should this just override the parent update()?
        if self.pause != True:
            if self.x_dir > 0:
                self.set_left()
            elif self.x_dir < 0:
                self.set_right()
            self.x += self.speed*self.x_dir
        
    def pause_player(self):
        self.pause = True

    def unpause_player(self):
        self.pause = False


class NPC(CustSprite):
    pass

class Item(CustSprite):
    pass

class ItemEquip(Item):
    pass

class TextBubble(Item): #separate text from text box? Or one image?
    pass

    def draw(self,game_window):
        super().draw(game_window)


class Button(TextBubble):
    def __init__(self,x,y,normal_img,hover_img,action=None): #only need 2 images for button
        super().__init__(x,y,normal_img)
        self.hover_img = hover_img
        self.action = action

    def set_click_response(self,action):
        self.action = action #lambda

    def update(self,event):
        mouse_pos = pygame.mouse.get_pos()
        if self.get_obj_rect().collidepoint(mouse_pos): #mouse hovering
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
            
    '''
    def resize_for_win(self,win_tuple):
        self.bg = resize_for_win_logic(self.bg,win_tuple)
        if self.mg != None:
            self.mg = resize_for_win_logic(self.mg,win_tuple)
        if self.fg != None:
            self.fg = resize_for_win_logic(self.fg,win_tuple)
        for x in self.sprites:
            x.resize_for_win(win_tuple)
    '''

class StateWalk(State):
    '''
    def __init__(self,number,bg,mg,fg,events,sprites):
        super().__init__(self,number,bg,mg,fg,events,sprites)
    '''

    def get_player(self):
        return self.sprites[0]

class StateTalk(State):
    def test(self):
        pass

