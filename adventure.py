# -*- coding: utf-8 -*-
"""
Text Adventure Game
An adventure in making adventure games.

To test your current solution, run the `test_my_solution.py` file.

Refer to the instructions on Canvas for more information.

"I have neither given nor received help on this assignment."
author: Taotao Wang
"""
__version__ = 8

# 2) print_introduction: Print a friendly welcome message for your game

# 3) get_initial_state: Create the starting player state dictionary

# 4) print_current_state: Print some text describing the current game world

# 5) get_options: Return a list of commands available to the player right now

# 6) print_options: Print out the list of commands available    

# 7) get_user_input: Repeatedly prompt the user to choose a valid command

# 8) process_command: Change the player state dictionary based on the command

# 9) print_game_ending: Print a victory, lose, or quit message at the end    
        
# Command Paths to give to the unit tester
WIN_PATH = ["Enter Dietrick Dinning Hall","Enter DXpress","Purchase Chicken Tender","Take a Honey Mustard","Check Out","Leave DXpress","Leave Dietrick Dinning Hall","Enter Dorm"]
LOSE_PATH = ["Enter Dorm"]

# 1) Main function that runs your game, read it over and understand
# how the player state flows between functions.
def main():
    # Print an introduction to the game
    print_introduction()
    # Make initial state
    the_player = get_initial_state()
    # Check victory or defeat
    while the_player['game status'] == 'playing':
        # Give current state
        print_current_state(the_player)
        # Get options
        available_options = get_options(the_player)
        # Give next options
        print_options(available_options)
        # Get Valid User Input
        chosen_command = get_user_input(available_options)
        # Process Commands and change state
        process_command(chosen_command, the_player)
    # Give user message
    print_game_ending(the_player)
def print_introduction():
    print("Welcome to the game of Tenders")
    print("You will need to be 10 out of 10 satisfication to win the game")
    print("Oh and don't starve to death")
    print("Type quit at anytime to quit the game")
    pass

def get_initial_state():
    state = {"game status":"playing",
             "location":"Yard",
             "hungry":5,
             "satisfication":0}
    return state
'''
Set an initial status
output : state
'''
def print_current_state(state):
    print("Your current location is:")
    print(state["location"])
    return
'''
Print current location
Output: None
'''
def get_options(state):
    locat = state["location"]
    state["hungry"] = state["hungry"] - 1
    opt = 0
    if locat == "Yard":
        opt = ["Enter Dietrick Dinning Hall","Enter Dorm"]
    elif locat == "Dietrick Dinning Hall":
        opt = ["Enter D2","Enter DXpress","Leave Dietrick Dinning Hall"]
    elif locat == "D2":
        opt = ["Leave D2"]
    elif locat == "DXpress":
        opt = ["Purchase Grilled Chicken with Cheese","Purchase Chicken Tender","Leave DXpress","Check Out"]
    elif locat == "Chicken Tender":
        opt = ["Take a Honey Mustard","Take a Ketchup","Check Out"]
    
    return opt
'''
Output: opt(options at this location)
'''
def print_options(opt):
    print("Here are your current optioins:")
    for choice in opt:
        print(choice)
    return

def get_user_input(opt):
    userinput = "x"
    while True:
        if userinput == "quit":
            break
        else:
            if userinput in opt:
                break
            else:
                userinput = input("Please input command exactly as shown: ")
    return userinput
'''
let's the user input which command they want to choose.
If user input somethin not a choice
it will ask the user to input again
output: userinput
'''
def process_command(userinput,state):
    if userinput == "quit":
        state["game status"] = "quit"
    else:
        if userinput == "Leaving Dinning Hall":
            state["location"] = "Yard"
        elif userinput == "Enter Dietrick Dinning Hall":
            state["location"] = "Dietrick Dinning Hall"
        elif userinput == "Enter D2":
            print("Food here is not so bad")
            state["satisfication"] = state["satisfication"] + 2
            state["location"] = "D2"
        elif userinput == "Leaving D2":
            state["location"] = "Dietrick Dinning Hall"
        elif userinput == "Enter DXpress":
            state["location"] = "DXpress"
        elif userinput == "Purchase Grilled Chicken with Cheese":
            state["satisfication"] = state["satisfication"] + 2
        elif userinput == "Purchase Chicken Tender":
            state["location"] = "Chicken Tender"
            state["satisfication"] = state["satisfication"] + 5
            state["hungry"] = state["hungry"] + 5
        elif userinput == "Take a Honey Mustard":
            state["satisfication"] = state["satisfication"] + 5
        elif userinput == "Take a Ketchup":
            print("It tastes like sxxt.")
            state["satisfication"] = state["satisfication"] -2
        elif userinput == "Check Out":
            print("Thank God I have a meal plan")
            state["location"] = "DXpress"
        elif userinput == "Leave DXpress":
            state["location"] = "Dietrick Dinning Hall"
        elif userinput == "Leave Dietrick Dinning Hall":
            state["location"] = "Yard"
        elif userinput == "Enter Dorm":
            if state["hungry"] > 0:
                if state["satisfication"] >= 10:
                    print("What a wonderful day!")
                    print("Chicken Tender is Great!!!!!")
                    state["game status"] = "win"
                else:
                    print("You are not satisfied with your food.")
                    state["game status"] = "lose"
            else:
                print("You didn't get enough food")
                state["game status"] = "lose"
    return
'''
Excute the user's input
'''
def print_game_ending(state):
    if state["game status"] == "win":
        print("You win the game!!!")
    elif state["game status"] == "lose":
        print("You lose")
        print("Don't Worry, Refresh the page and start again!")
    elif state["game status"] == "quit":
        print("You don't like this amazing game?")
    elif state["game status"] == "playing":
        print("keep going")
    return
'''
Explain if you win the game or not
'''
    
# Executes the main function
if __name__ == "__main__":
    '''
    You might comment out the main function and call each function
    one at a time below to try them out yourself '''
    main()
    ## e.g., comment out main() and uncomment the line(s) below
    # print_introduction()
    # print(get_initial_state())
    # ...