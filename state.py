#state objects- where to render text bubbles and buttons? separate file?
from img_loader import *
from obj_class import *
from button_functions import *

start_button = Button(300,150,game_buttons_img[0],game_buttons_img[1],lambda:3)
quit_button1 = Button(500,150,game_buttons_img[6],game_buttons_img[7],lambda:'QUIT')
quit_button2 = Button(200,250,game_buttons_img[6],game_buttons_img[7],lambda:'QUIT')
resume_button = Button(200,50,game_buttons_img[4],game_buttons_img[5])
restart_button = Button(200,150,game_buttons_img[2],game_buttons_img[3],lambda:'RESTART')

user = Player(player1,player2,player3)

#quit_button2.set_click_response(lambda: 'QUIT')
#restart_button.set_click_response(lambda: 'RESTART')

menu_state1 = State(1,great_wave,great_wave,great_wave,[],[start_button,quit_button1])
menu_state2 = State(2,great_wave,great_wave,great_wave,[],[resume_button,restart_button,quit_button2])
s1 = State(3,great_wave,great_wave,great_wave,[],[user])

state_dict = {1:menu_state1,2:menu_state2,3:s1} #translation
