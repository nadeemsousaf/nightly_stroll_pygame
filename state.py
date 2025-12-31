#state objects- where to render text bubbles and buttons? separate file?
from img_loader import *
from obj_class import *

window_size = (800,500)

start_button = Button(300,150,game_buttons_img[0],game_buttons_img[1],lambda:3)
quit_button1 = Button(500,150,game_buttons_img[6],game_buttons_img[7],lambda:'QUIT')
quit_button2 = Button(200,250,game_buttons_img[6],game_buttons_img[7],lambda:'QUIT')
resume_button = Button(200,50,game_buttons_img[4],game_buttons_img[5])
restart_button = Button(200,150,game_buttons_img[2],game_buttons_img[3],lambda:4)
yes_restart_button = Button(200,200,game_buttons_img[2],game_buttons_img[3],lambda:'RESTART')
test_button = Button(200,150,game_buttons_img[2],game_buttons_img[3],lambda:5)
test_button2 = Button(200,150,game_buttons_img[2],game_buttons_img[3],lambda:3)

user = Player(0,245,my_guy1,my_guy2,my_guy5,my_guy3,my_guy6,my_guy4)

#quit_button2.set_click_response(lambda: 'QUIT')
#restart_button.set_click_response(lambda: 'RESTART')

menu_state1 = State(1,[],[start_button,quit_button1],title_test)
menu_state2 = State(2,[],[resume_button,restart_button,quit_button2],title_test)
menu_state3 = State(2,[],[yes_restart_button],are_you_sure)
s1 = StateWalk(3,[],[user,test_button],great_wave)
s2 = StateTalk(3,[],[test_button2],great_wave)

#translation
state_dict = {
    1:menu_state1,
    2:menu_state2,
    3:s1,
    4:menu_state3,
    5:s2
    }
