#state objects- where to render text bubbles and buttons? separate file?
from img_loader import *
from obj_class import *
start_button = Button(200,50,startBN_img,startBA_img,"F")
quit_button1 = Button(0,100,quitBN,quitBA,"L")
quit_button2 = Button(0,400,quitBN,quitBA,"L")
resume_button = Button(0,0,resumeBN,resumeBA,"R")
restart_button = Button(0,0,restartBN,restartBA,"F")
state1 = State(1,great_wave,great_wave,great_wave,[],[start_button])

state_dict = {1:state1} #translation
