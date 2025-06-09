from sys import exit
from pathlib import Path
import json
from state import *
from npc import *
from tree import *

pygame.init()
window = pygame.display.set_mode((800,500))
pygame.display.set_caption('Nightly Stroll')
clock = pygame.time.Clock()

global_dict = {"game_state":1, "item":"broad sword", "city":"New York"} #default global values, test values rn
mem_file = Path("NightlyStrollMem.txt")
if mem_file.exists():
    file = open(mem_file, "r")
    global_dict = json.loads(file.read())
    file.close()
else:
    file = open(mem_file, "x")
    file.close()

player = Player(test,test,test) #temporary

'''
while running:
    keys = pygame.key.get_pressed()  # Checking pressed keys
    if keys[pygame.K_UP]:
        y1 -= 1
    if keys[pygame.K_DOWN]:
        y1 += 1
'''


while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            file = open("NightlyStrollMem.txt", "w") #open memory file
            json.dump(global_dict, file) #write updated json of globals
            file.close() #close memory file
            exit() #exit program
    
    state_dict[global_dict["game_state"]].update()
    state_dict[global_dict["game_state"]].draw(window)
    pygame.display.update()
    clock.tick(40)