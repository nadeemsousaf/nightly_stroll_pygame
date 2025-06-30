from sys import exit
from pathlib import Path
import json
from state import *
from npc import *
from tree import *

pygame.init()
window = pygame.display.set_mode((800,500), pygame.RESIZABLE)
pygame.display.set_caption('Nightly Stroll')
clock = pygame.time.Clock()

load_state = menu_state1
global_dict = {"game_state":1, "item":"broad sword", "city":"New York"} #default global values, test values rn
mem_file = Path("NightlyStrollMem.txt")
if mem_file.exists():
    load_state = menu_state2
    file = open(mem_file, "r")
    global_dict = json.loads(file.read())
    file.close()
else:
    file = open(mem_file, "x")
    file.close()

player = Player(test,test,test) #temporary

while True: #game loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            file = open("NightlyStrollMem.txt", "w") #open memory file
            json.dump(global_dict, file) #write updated json of globals
            file.close() #close memory file
            exit() #exit program
    
    re = load_state.update(event)
    if re != None: #changing state
        load_state = re
        load_state.update(event)
    load_state.draw(window)
   
    pygame.display.update()
    clock.tick(40)