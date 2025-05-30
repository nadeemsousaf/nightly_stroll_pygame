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

#check if memory file exists in current directory
#if exists, set globals- must parse
#if not, create file and write default globals to file + set defaults in flow.py scope
global_dict = {"game_state":1, "item":"broad sword", "city":"New York"} #default global values, test values rn
mem_file = Path("NightlyStrollMem.txt")
if mem_file.exists():
    file = open(mem_file, "r")
    global_dict = json.loads(file.read())
    file.close()
else:
    file = open(mem_file, "x")
    file.close()

player = Player(test,test,test)

while True:
    if global_dict["game_state"] == 0:
        print("do this")
    elif global_dict["game_state"] == 1:
        print("do that")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            file = open("NightlyStrollMem.txt", "w") #open memory file
            json.dump(global_dict, file) #write updated json of globals
            file.close() #close memory file
            exit() 
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

    #window.blit(state.bg, (0,0))
    #window.blit(state.fg, (0,70))
    #add objects in the state, probably held in a list
    pygame.display.update()
    clock.tick(40)