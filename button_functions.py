from flow import global_dict, mem_file

#make specific lambdas to add specific items per button and pass to button class
def add_to_inventory(name,item):
    global_dict[name] = item

def restart():
    x = 10
    #reset the dict and write it to file

def resume():
    x = 10
    #maybe not needed, could just pass the state inside the saved dict

def quit():
    x = 10
    #can we end program from here?