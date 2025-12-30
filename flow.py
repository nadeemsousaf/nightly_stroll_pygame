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

def shutdown_save():
    pygame.quit()
    file = open("NightlyStrollMem.txt", "w") #open memory file
    json.dump(global_dict, file) #write updated json of globals
    file.close() #close memory file
    exit() #exit program

def restart_game():
    global load_state
    global global_dict
    load_state = menu_state1
    global_dict = {"game_state":1, "item":"broad sword", "city":"New York"}

add_item_code = {} #code with function

player = Player(0,0,my_guy1,my_guy2,my_guy5,my_guy3,my_guy6,my_guy4) #placeholder

while True: #game loop
    if load_state is StateWalk:
        player = load_state.get_player() #set player for movement
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shutdown_save()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                #player.set_y_dir(1)
                player.set_forward()
            elif event.key == pygame.K_UP:
                #player.set_y_dir(-1)
                player.set_forward()
            elif event.key == pygame.K_LEFT:
                player.set_x_dir(-1)
                player.set_right()
            elif event.key == pygame.K_RIGHT:
                player.set_x_dir(1)
                player.set_left()
            '''
            elif event.key == pygame.K_SPACE:
                player.attack()
            '''
        if event.type == pygame.KEYUP:
            player = load_state.get_player() #set player for movement
            if event.key == pygame.K_DOWN:
                player.set_y_dir(0)
            elif event.key == pygame.K_UP:
                player.set_y_dir(0)
            elif event.key == pygame.K_LEFT:
                player.set_x_dir(0)
            elif event.key == pygame.K_RIGHT:
                player.set_x_dir(0)

    re = load_state.update(event) #custom handling
    if re != None: #changing state
        if re == 'QUIT':
            shutdown_save()
        elif re == 'RESTART':
            restart_game()
        elif re in add_item_code:
            add_item_code[re]
        else: #change game state
            load_state = state_dict[re]
            #load_state = re
            load_state.update(event) 
    load_state.draw(window)
   
    pygame.display.update()
    clock.tick(40)