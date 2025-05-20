class Player():
    def __init__(self, front, left, right):
        self.show = front
        self.front = front
        self.left = left
        self.right = right
        self.x = 0
        self.y = 245
        self.x_dir = 0
        self.y_dir = 0
        self.speed = 10
        self.health = 200
    def draw(self):
        print("placeholder")

class NPC():
    def __init__(self, x, y, normal_img, dialogue_list, movements_list):
        self.x = x
        self.y = y
        self.show = normal_img
        self.normal_img = normal_img
        self.dialogue_list = dialogue_list
        self.movements_list = movements_list
        self.health = 100
    def draw(self):
        print("placeholder")
    def motion(self): #speak and/or move during user interaction
        print("placeholder")

class TextBubble():
    def __init__(self,text,x,y,font,fg,bg):
        self.text = text
        self.x = x
        self.y = y
        self.font = font
        self.fg = fg
        self.bg = bg
    def draw(self):
        print("placeholder")

class Node():
    def __init__(self,data):
        self.data = data
        self.next = None
    def set_next(self,next):
        self.next = next

class State():
    def __init__(self,number,bg,mg,fg,exit_x,current):
        self.number = number
        self.bg = bg
        self.mg = mg
        self.fg = fg
        self.exit_x = exit_x
        self.current = current #current event inside State, is a Node
        self.exit = False
    def draw(self):
        print("placeholder")
    def open_exit(self):
        self.exit = True