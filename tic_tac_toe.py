#Tic Tac Toe Game
#By Joshua Herman
#For CSE210 Assignment: "W02 Introduction: Ponder and Prove"
#
#main function
def main():
    #Welcome message
    print("Welcome to Tic Tac Toe\nBy Joshua Herman\n-------------------------------")
    print("\nTo begin let's setup the game:")
    game_setup_conf = False
    while game_setup_conf == False:
        options = game_setup()
        board_size = options[0]
        if board_size == "1":
            board_size_name = "3x3"
        elif board_size == "2":
            board_size_name = "4x4"
        elif board_size =="3":
            board_size_name = "5x5"
        player_x = options[1]
        player_y = options[2]
        game_setup_confirm = input(f"Please confirm the following:\n\nBoard Size: {board_size_name}\nPlayer X's Name: {player_x}\nPlayer Y's Name: {player_y}\nPlease confirm by typing Y or N: ")
        if game_setup_confirm.lower() == "y" or game_setup_confirm.lower() == "yes":
            game_setup_conf = True
        else:
            print("\nRe-running Setup...")
    print("end test")
        
#Game Setup Function
def game_setup():
    board_selection_conf = False
    while board_selection_conf == False:
        board_selection = input("\nBoard Sizes:\n\n1. 3x3 (Classic)\n2. 4x4 (Medium)\n3. 5x5 (Large)\n\nPlease select your board size by typing a number listed above (1-3): ")
        if board_selection == "1" or board_selection == "2" or board_selection == "3":
            board_selection_conf = True
        else:
            print("\nSorry that was not one of the options available above, please try again.")
    player_x = input("\nPlease enter the name for the first player (X), or press enter to use the default: ")
    if player_x == "":
        player_x = "X"
    player_y = input("\nPlease enter the name for the second player (Y), or press enter to use the default: ")
    if player_y == "":
        player_y = "Y"
    options = [board_selection, player_x, player_y]
    return options
#Run Program
main()