from sys import exit
from pathlib import Path
import json
from state import *
from npc import *
from tree import *

pygame.init()
window = pygame.display.set_mode(window_size, pygame.RESIZABLE)
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

player = Player(0,0,[my_guy1,my_guy2],[my_guy5,my_guy3],[my_guy6,my_guy4]) #placeholder

while True: #game loop
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            shutdown_save()

        if event.type == pygame.KEYDOWN and isinstance(load_state,StateWalk):
            player = load_state.get_player() #set player for movement
            if event.key == pygame.K_DOWN:
                player.set_forward()
            elif event.key == pygame.K_UP:
                player.set_forward()
            elif event.key == pygame.K_LEFT:
                player.set_x_dir(-1)
            elif event.key == pygame.K_RIGHT:
                player.set_x_dir(1) 
                
            '''
            elif event.key == pygame.K_SPACE:
                player.attack()
            '''
        if event.type == pygame.KEYUP and isinstance(load_state,StateWalk):
            player = load_state.get_player() #set player for movement
            if event.key == pygame.K_DOWN:
                player.set_y_dir(0)
            elif event.key == pygame.K_UP:
                player.set_y_dir(0)
            elif event.key == pygame.K_LEFT:
                player.set_x_dir(0)
            elif event.key == pygame.K_RIGHT:
                player.set_x_dir(0)

        if isinstance(load_state,StateWalk): #working on screen out-of-bounds -> image extra space around character?
            #print(f'player: {player.x}| window:{window.get_size()[0]}')
            if player.x < 0:
                player.x = 0
            if player.x > window.get_size()[0]:
                player.x = window.get_size()[0] - player.get_obj_rect().width
                
        if event.type == pygame.VIDEORESIZE:
            '''
            for i in state_dict:
                state_dict[i].resize_for_win((window_size,window.get_size()))
            '''
            window_size = window.get_size()

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
            load_state.update(event) 
    load_state.draw(window)
   
    pygame.display.update()
    clock.tick(40)