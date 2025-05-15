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
    def __init__(self, x, y, normal):
        self.x = x
        self.y = y
        self.show = normal
        self.normal = normal
        self.health = 100
    def attack(self):
        print("placeholder")
    def vanquish(self):
        print("placeholder")
