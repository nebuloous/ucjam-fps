# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Main Character")
default tw_kills = {1: True, 2: True, 3: True, 4: True, 5: True}
default a_kills = {1: True, 2: True, 3: True, 4: True, 5: True}

# TWO WEEKS GAME SCREEN
screen tw_game():
    zorder 1 
    for i in range(1,6):
        imagebutton:
            idle "tw_enemy" + str(i) + ".png"
            hover "tw_enemy" + str(i) + "hover.png"
            selected_idle Null()
            selected_hover Null()
            focus_mask True
            action [SetDict(tw_kills, i, False), Return()]

# ALORANT GAME SCREEN
screen a_game():
    zorder 1 
    for i in range(1,6):
        imagebutton:
            idle "a_enemy" + str(i) + ".png"
            hover "a_enemy" + str(i) + "hover.png"
            selected_idle Null()
            selected_hover Null()
            focus_mask True
            action [SetDict(a_kills, i, False), Return()]

# The game starts here.

label start:

    # Show a background.
    scene bg room

    # These display lines of dialogue.
    m "This is test dialogue before the next screen."

    menu:
        "What game should I play?"

        "Alorant":
            jump alorant
        "Two Weeks":
            jump two_weeks

#### SCENE WHERE MC PLAYS ALORANT
label alorant:
    scene bg alorant
    m "Let's goooo!"
    while a_kills[1] == True or a_kills[2] == True or a_kills[3] == True or a_kills[4] == True or a_kills[5] == True:
        call screen a_game 
    jump a_end

label a_end:
    m "GGEZ!"
    jump end #jump to next section, end here is for testing

#### SCENE WHERE MC PLAYS TWO WEEKS
label two_weeks:
    scene bg twoweeks
    m "Let's get 'em!"
    while tw_kills[1] == True or tw_kills[2] == True or tw_kills[3] == True or tw_kills[4] == True or tw_kills[5] == True:
        #block of code to run 
        call screen tw_game 
    jump tw_end #jump to next section, end here is for testing

label tw_end:
    m "Get pwned nerd"
    jump end 

label end:
    scene bg room
    m "We did it!"
    # This ends the game.

    return
