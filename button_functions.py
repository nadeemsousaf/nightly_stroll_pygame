from flow import global_dict

def add_to_inventory(name,item):
    global_dict[name] = item

#make specific lambdas to add specific items per button and pass to button class