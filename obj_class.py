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
    def vanquish(self):
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
    def attack(self):
        print("placeholder")
    def vanquish(self):
        print("placeholder")

class State():
    def __init__(self,number,bg,mg,fg):
        self.number = number
        self.bg = bg
        self.mg = mg
        self.fg = fg

class TextBubble():
    def __init__(self):
        print("ok")

class StateText():
    def __init__(self):
        print("ok")
