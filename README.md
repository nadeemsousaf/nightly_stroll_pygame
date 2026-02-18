Name: Nadeem Sousaf

Developer notes:
Working on next;
- creating spritesheet & backgrounds -> adapt code to handle spritesheets
- window textbox -> adjust to background size, text wrapping, user input
- window resizing -> adjusting elements within window
- different view perspectives
- screen bounds when walking
- equipable items

Program Description: RPG-style game made using Pygame

Execution Instructions: Type "python flow.py" into terminal, then follow instructions in the GUI (appears as a window) to play. Currently, if you wish to reset the game, you must delete "NightlyStrollMem.txt" from the working directory as the action would delete all saved game data (this will eventually be updated).

File Overview:
flow.py: control flow of the game
dialogue.py: contains all dialogue
obj_class.py: contains class definitions
tree.py: creates storyline tree
state.py: creates State objects
npc.py: creates NPC objects
img_loader.py: loads pygame images
button_functions.py: contains button functions, held under "action" in the button class
NightlyStrollMem.txt: contains saved game data
?file(s) for Motion, NodeL, Button, TextBubble objects?

Citations: