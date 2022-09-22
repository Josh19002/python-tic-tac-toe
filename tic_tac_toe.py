#Tic Tac Toe Game
#By Joshua Herman
#For CSE210 Assignment: "W02 Introduction: Ponder and Prove"

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
        game_setup_confirm = input(f"\nPlease confirm the following:\n\nBoard Size: {board_size_name}\nPlayer X's Name: {options[1]}\nPlayer O's Name: {options[2]}\n\nPlease confirm by typing Y or N: ")
        if game_setup_confirm.lower() == "y" or game_setup_confirm.lower() == "yes":
            game_setup_conf = True
        else:
            print("\nRe-running Setup...")
    replay = True
    while replay == True:
        run_game(options)
        replay_ask = input("Would you like to play again? (Y or N): ")
        if replay_ask.lower() == "y":
            print("\nOk! Re-running Setup...")
            game_setup_conf = False
            while game_setup_conf == False:
                options = game_setup()
                board_size = options[0]
                if board_size == "1":
                    board_size_name = "3x3"
                elif board_size == "2":
                    board_size_name = "4x4"
                game_setup_confirm = input(f"\nPlease confirm the following:\n\nBoard Size: {board_size_name}\nPlayer X's Name: {options[1]}\nPlayer O's Name: {options[2]}\n\nPlease confirm by typing Y or N: ")
                if game_setup_confirm.lower() == "y" or game_setup_confirm.lower() == "yes":
                    game_setup_conf = True
                else:
                    print("\nRe-running Setup...")
        else:
            print("\nThank you for playing!\n")
            replay = False
    
        
#Game Setup Function
def game_setup():
    board_selection_conf = False
    while board_selection_conf == False:
        board_selection = input("\nBoard Sizes:\n\n1. 3x3 (Classic)\n2. 4x4 (Large)\n\nPlease select your board size by typing a number listed above (1-2): ")
        if board_selection == "1" or board_selection == "2":
            board_selection_conf = True
        else:
            print("\nSorry that was not one of the options available above, please try again.")
    player_x = input("\nPlease enter the name for the first player (X), or press enter to use the default: ")
    if player_x == "":
        player_x = "X"
    player_o = input("\nPlease enter the name for the second player (O), or press enter to use the default: ")
    if player_o == "":
        player_o = "O"
    options = [board_selection, player_x, player_o]
    return options

#Game
def run_game(options):
    print("\n\n\n\n\n\n\n\nLets Play!\nGet 3 in a row to win!\n-----------------------------")
    game_won = False
    board_size = options[0]
    player_turn = "X"
    if board_size == "1":
        board=["1","2","3","4","5","6","7","8","9"]
    elif board_size == "2":
        board=["1","2","3","4","5","6","7","8","9","10","11","12","13","14","15","16"]
    while game_won == False:
            display_board(board, board_size)
            #Player Name For Current Player
            if player_turn == "X":
                current_player = options[1] + " (X)"
            else:
                current_player = options[2] + " (O)"
            #Player Turn
            move = input(f"\n{current_player} it is your turn.\nSelect the space you want to claim by typing it's number: ")
            if check_move(move, board):
                move = int(move)
                move = move-1
                if board_size == "1":
                    if player_turn == "X":
                        board[move] = f"\033[91m{player_turn}\033[00m"
                    else:  
                        board[move] = f"\033[92m{player_turn}\033[00m"
                else:
                    if move >= 9:
                        if player_turn == "X":
                            board[move] = f"\033[91m {player_turn}\033[00m"
                        else:  
                            board[move] = f"\033[92m {player_turn}\033[00m"
                    else:
                        if player_turn == "X":
                            board[move] = f"\033[91m{player_turn}\033[00m"
                        else:  
                            board[move] = f"\033[92m{player_turn}\033[00m"
                #End of turn player swap
                if player_turn == "X":
                    player_turn = "O"
                else:
                    player_turn = "X"
                winner = win_check(board, board_size)
                if winner == "x":
                    print("\nGAME OVER")
                    display_board(board, board_size)
                    print(f"\n{options[1]} is the winner!")
                    game_won = True
                elif winner == "o":
                    print("\nGAME OVER")
                    display_board(board, board_size)
                    print(f"\n{options[2]} is the winner!")
                    game_won = True
                elif winner == "cat":
                    print("\nGAME OVER")
                    display_board(board, board_size)
                    print("\nIt's a draw!")
                    game_won = True
            else:
                print("\nThat move was not valid, please try again.")
#Display Board
def display_board(board, board_size):
    if board_size == "1":
        print(f"\n{board[0]}|{board[1]}|{board[2]}\n-+-+-\n{board[3]}|{board[4]}|{board[5]}\n-+-+-\n{board[6]}|{board[7]}|{board[8]}")
    elif board_size == "2":
        print(f"\n {board[0]}| {board[1]}| {board[2]}| {board[3]}\n--+--+--+--\n {board[4]}| {board[5]}| {board[6]}| {board[7]}\n--+--+--+--\n {board[8]}|{board[9]}|{board[10]}|{board[11]}\n--+--+--+--\n{board[12]}|{board[13]}|{board[14]}|{board[15]}")
#Move Checks
def check_move(move, board):
    if move in board:
        return True
    else:
        return False
#Game End Check
def win_check(board, board_size):
        #Board 1 Checks
        if board_size == "1":
            #X Checks
            #Rows
            if board[0] == "\x1b[91mX\x1b[00m" and board[1] == "\x1b[91mX\x1b[00m" and board[2] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[3] == "\x1b[91mX\x1b[00m" and board[4] == "\x1b[91mX\x1b[00m" and board[5] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[6] == "\x1b[91mX\x1b[00m" and board[7] == "\x1b[91mX\x1b[00m" and board[8] == "\x1b[91mX\x1b[00m":
                return "x"
            #Columns
            elif board[0] == "\x1b[91mX\x1b[00m" and board[3] == "\x1b[91mX\x1b[00m" and board[6] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[1] == "\x1b[91mX\x1b[00m" and board[4] == "\x1b[91mX\x1b[00m" and board[7] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[2] == "\x1b[91mX\x1b[00m" and board[5] == "\x1b[91mX\x1b[00m" and board[8] == "\x1b[91mX\x1b[00m":
                return "x"
            #Diagonals
            elif board[0] == "\x1b[91mX\x1b[00m" and board[4] == "\x1b[91mX\x1b[00m" and board[8] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[2] == "\x1b[91mX\x1b[00m" and board[4] == "\x1b[91mX\x1b[00m" and board[6] == "\x1b[91mX\x1b[00m":
                return "x"
            #O Checks
            #Rows
            if board[0] == "\x1b[92mO\x1b[00m" and board[1] == "\x1b[92mO\x1b[00m" and board[2] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[3] == "\x1b[92mO\x1b[00m" and board[4] == "\x1b[92mO\x1b[00m" and board[5] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[6] == "\x1b[92mO\x1b[00m" and board[7] == "\x1b[92mO\x1b[00m" and board[8] == "\x1b[92mO\x1b[00m":
                return "o"
            #Columns
            elif board[0] == "\x1b[92mO\x1b[00m" and board[3] == "\x1b[92mO\x1b[00m" and board[6] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[1] == "\x1b[92mO\x1b[00m" and board[4] == "\x1b[92mO\x1b[00m" and board[7] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[2] == "\x1b[92mO\x1b[00m" and board[5] == "\x1b[92mO\x1b[00m" and board[8] == "\x1b[92mO\x1b[00m":
                return "o"
            #Diagonals
            elif board[0] == "\x1b[92mO\x1b[00m" and board[4] == "\x1b[92mO\x1b[00m" and board[8] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[2] == "\x1b[92mO\x1b[00m" and board[4] == "\x1b[92mO\x1b[00m" and board[6] == "\x1b[92mO\x1b[00m":
                return "o"
            #None
            elif board[0] != "1" and board[1] != "2" and board[2] != "3" and board[3] != "4" and board[4] != "5" and board[5] != "6" and board[6] != "7" and board[7] != "8" and board[8] != "9":
                return "cat"
            else:
                return ""
        #Board 2 Checks
        elif board_size == "2":
            #Large Board Quadrent 1
            #X Checks
            #Rows
            if board[0] == "\x1b[91mX\x1b[00m" and board[1] == "\x1b[91mX\x1b[00m" and board[2] == "\x1b[91mX\x1b[00m" and board[3] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[4] == "\x1b[91mX\x1b[00m" and board[5] == "\x1b[91mX\x1b[00m" and board[6] == "\x1b[91mX\x1b[00m" and board[7] == "\x1b[91mX\x1b[00m":
                return "x"
            elif board[8] == "\x1b[91mX\x1b[00m" and board[9] == "\x1b[91m X\x1b[00m" and board[10] == "\x1b[91m X\x1b[00m" and board[11] == "\x1b[91m X\x1b[00m":
                return "x"
            elif board[12] == "\x1b[91m X\x1b[00m" and board[13] == "\x1b[91m X\x1b[00m" and board[14] == "\x1b[91m X\x1b[00m" and board[15] == "\x1b[91m X\x1b[00m":
                return "x"
            #Columns
            elif board[0] == "\x1b[91mX\x1b[00m" and board[4] == "\x1b[91mX\x1b[00m" and board[8] == "\x1b[91mX\x1b[00m" and board[12] == "\x1b[91m X\x1b[00m":
                return "x"
            elif board[1] == "\x1b[91mX\x1b[00m" and board[5] == "\x1b[91mX\x1b[00m" and board[9] == "\x1b[91m X\x1b[00m" and board[13] == "\x1b[91m X\x1b[00m":
                return "x"
            elif board[2] == "\x1b[91mX\x1b[00m" and board[6] == "\x1b[91mX\x1b[00m" and board[10] == "\x1b[91m X\x1b[00m" and board[14] == "\x1b[91m X\x1b[00m":
                return "x"
            elif board[3] == "\x1b[91mX\x1b[00m" and board[7] == "\x1b[91mX\x1b[00m" and board[11] == "\x1b[91m X\x1b[00m" and board[15] == "\x1b[91m X\x1b[00m":
                return "x"
            #Diagonals
            elif board[0] == "\x1b[91mX\x1b[00m" and board[5] == "\x1b[91mX\x1b[00m" and board[10] == "\x1b[91m X\x1b[00m" and board[15] == "\x1b[91m X\x1b[00m":
                return "x"
            elif board[3] == "\x1b[91mX\x1b[00m" and board[6] == "\x1b[91mX\x1b[00m" and board[9] == "\x1b[91m X\x1b[00m" and board[12] == "\x1b[91m X\x1b[00m":
                return "x"
            #O Checks
            #Rows
            elif board[0] == "\x1b[92mO\x1b[00m" and board[1] == "\x1b[92mO\x1b[00m" and board[2] == "\x1b[92mO\x1b[00m" and board[3] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[4] == "\x1b[92mO\x1b[00m" and board[5] == "\x1b[92mO\x1b[00m" and board[6] == "\x1b[92mO\x1b[00m" and board[7] == "\x1b[92mO\x1b[00m":
                return "o"
            elif board[8] == "\x1b[92mO\x1b[00m" and board[9] == "\x1b[92m O\x1b[00m" and board[10] == "\x1b[92m O\x1b[00m" and board[11] == "\x1b[92m O\x1b[00m":
                return "o"
            elif board[12] == "\x1b[92m O\x1b[00m" and board[13] == "\x1b[92m O\x1b[00m" and board[14] == "\x1b[92m O\x1b[00m" and board[15] == "\x1b[92mvO\x1b[00m":
                return "o"
            #Columns
            elif board[0] == "\x1b[92mO\x1b[00m" and board[4] == "\x1b[92mO\x1b[00m" and board[8] == "\x1b[92mO\x1b[00m" and board[12] == "\x1b[92m O\x1b[00m":
                return "o"
            elif board[1] == "\x1b[92mO\x1b[00m" and board[5] == "\x1b[92mO\x1b[00m" and board[9] == "\x1b[92m O\x1b[00m" and board[13] == "\x1b[92m O\x1b[00m":
                return "o"
            elif board[2] == "\x1b[92mO\x1b[00m" and board[6] == "\x1b[92mO\x1b[00m" and board[10] == "\x1b[92m O\x1b[00m" and board[14] == "\x1b[92m O\x1b[00m":
                return "o"
            elif board[3] == "\x1b[92mO\x1b[00m" and board[7] == "\x1b[92mO\x1b[00m" and board[11] == "\x1b[92m O\x1b[00m" and board[15] == "\x1b[92m O\x1b[00m":
                return "o"
            #Diagonals
            elif board[0] == "\x1b[92mO\x1b[00m" and board[5] == "\x1b[92mO\x1b[00m" and board[10] == "\x1b[92m O\x1b[00m" and board[15] == "\x1b[92m O\x1b[00m":
                return "o"
            elif board[3] == "\x1b[92mO\x1b[00m" and board[6] == "\x1b[92mO\x1b[00m" and board[9] == "\x1b[92m O\x1b[00m" and board[12] == "\x1b[92m O\x1b[00m":
                return "o"

            #None
            elif board[0] != "1" and board[1] != "2" and board[2] != "3" and board[3] != "4" and board[4] != "5" and board[5] != "6" and board[6] != "7" and board[7] != "8" and board[8] != "9" and board[9] != "10" and board[10] != "11" and board[11] != "12" and board[12] != "13" and board[13] != "14" and board[14] != "15" and board[15] != "16":
                return "cat"
            else:
                return ""
#Run Program
main()