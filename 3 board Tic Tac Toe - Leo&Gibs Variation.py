#Alonzo, John Leomarc (50%)
#Diwa, Gibson Marshall (50%)

#references/sources
# A sample code of an ordinary tic-tac-toe game : https://codereview.stackexchange.com/questions/108738/python-tic-tac-toe-game
#  How User defined functions work: https://www.codementor.io/kaushikpal/user-defined-functions-in-python-8s7wyc8k2
# How to use For loops: https://wiki.python.org/moin/ForLoop
#Lists - https://www.w3schools.com/python/python_lists.asp
#Range function - https://www.pythoncentral.io/pythons-range-function-explained/
#Python Exceptions (try) - https://realpython.com/python-exceptions/
#How to kill python code through script - https://stackoverflow.com/questions/543309/programmatically-stop-execution-of-python-script/543375

import time #Hehe just for the intro
# winwen is a global function used to count the number of boards left
winwen = 0
#range, list, win conditions, board output etc.
def threebord():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    end = False
#Win1 are the winning combinations for board 1, win2 for board 2 and win3 for board 3
    win1 = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win2 = ((10, 11, 12), (13, 14, 15), (16, 17, 18), (10, 13, 16), (11, 14, 17), (12, 15, 18), (10, 14, 18), (12, 14, 16))
    win3 = ((19, 20, 21), (22, 23, 24), (25, 26, 27), (19, 22, 25), (20, 23, 26), (21, 24, 27), (19, 23, 27), (21, 23, 25))
#blocks() is basically the board output
    def blocks():
        print(board[0], board[1], board[2], "       ", board[10], board[11], board[12], "       ", board[19], board[20], board[21])
        print(board[3], board[4], board[5], "       ", board[13], board[14], board[15], "       ", board[22], board[23], board[24])
        print(board[6], board[7], board[8], "       ", board[16], board[17], board[18], "       ", board[25], board[26], board[27])
        print()
#Since what is printed in the output is +1 of the actual board number, for example board[0] is 1, this just substracts the input from which the player made
#Also checks if the inputted number is in the range or if it is even a number
    def number():
        while True:
                x = input()
                try:
                    x  = int(x)
                    x = x - 1
                    if x in range(0, 28):
                        return x
# plop = number() return plop is basically just restarting the defined function if the input was invalid( c o n t i n u e)
                    else:
                        print("That's not on the board")
                        plop = number()
                        return plop
                except ValueError:
                   print("That's not a number")
                   plop = number()
                   return plop
#These two user defined functions, playerx and playero are the ones that manage the input of the players
    def playerx():
        n = number()
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playerx()
        else:
            board[n] = "X"

    def playero():
        n = number()
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playero()
        else:
            board[n] = "O"

#This user defined function is the most complicated one and most likely the core code of the game rules
# The global variable winwen is used to keep track of the number of boards left
#Count is used to keep track of the last player who won, either X or O
# A tie is activated if all tiles are placed on and winwen has not reached 3 which indicates that noone won the last board
#Win is the winning variable, equated to 1 and X wins equated to 2 and O wins

    def ending():
        global winwen
        tie = 0
        count = 0
        win = 0
        for x in win1:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the first board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[0] = "-"
                    board[1] = "-"
                    board[2] = "-"
                    board[3] = "-"
                    board[4] = "-"
                    board[5] = "-"
                    board[6] = "-"
                    board[7] = "-"
                    board[8] = "-"
                winwen = winwen + 1
                count = 1
#The parts here is how an extra turn was added, It was set to not work if winwen is equal to 3 because otherwise the program wouldn't end
#You can't get an extra turn if you ended the game with your last win right? xD
                if winwen != 3:
                    blocks()
                    print("Player X gets an extra turn! choose where to place an X")
                    playerx()
                    print()
                    ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("Player O won the first board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[0] = "-"
                    board[1] = "-"
                    board[2] = "-"
                    board[3] = "-"
                    board[4] = "-"
                    board[5] = "-"
                    board[6] = "-"
                    board[7] = "-"
                    board[8] = "-"
                count = 2
                winwen = winwen + 1
                if winwen != 3:
                    blocks()
                    print("Player O gets an extra turn! choose where to place an O")
                    playero()
                    print()
                    ending()
        for x in win2:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the second board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[10] = "-"
                    board[11] = "-"
                    board[12] = "-"
                    board[13] = "-"
                    board[14] = "-"
                    board[15] = "-"
                    board[16] = "-"
                    board[17] = "-"
                    board[18] = "-"
                count = 1
                winwen = winwen + 1
                if winwen != 3:
                    blocks()
                    print("Player X gets an extra turn! choose where to place an X")
                    playerx()
                    print()
                    ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
#Still Similar lines of code with different variables
                print("Player O won the second board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[10] = "-"
                    board[11] = "-"
                    board[12] = "-"
                    board[13] = "-"
                    board[14] = "-"
                    board[15] = "-"
                    board[16] = "-"
                    board[17] = "-"
                    board[18] = "-"
                winwen = winwen + 1
                count = 2
                if winwen != 3:
                    blocks()
                    print("Player O gets an extra turn! choose where to place an O")
                    playero()
                    print()
                    ending()
        for x in win3:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the third board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[19] = "-"
                    board[20] = "-"
                    board[21] = "-"
                    board[22] = "-"
                    board[23] = "-"
                    board[24] = "-"
                    board[25] = "-"
                    board[26] = "-"
                    board[27] = "-"
                winwen = winwen + 1
                count = 1
                if winwen != 3:
                    blocks()
                    print("Player X gets an extra turn! choose where to place an X")
                    playerx()
                    print()
                    ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("Player O won the third board!")
                if winwen == 0 or winwen == 1 or winwen == 2:
                    board[19] = "-"
                    board[20] = "-"
                    board[21] = "-"
                    board[22] = "-"
                    board[23] = "-"
                    board[24] = "-"
                    board[25] = "-"
                    board[26] = "-"
                    board[27] = "-"
                winwen = winwen + 1
                count = 2
                if winwen != 3:
                    blocks()
                    print("Player O gets an extra turn! choose where to place an O")
                    playero()
                    print()
                    ending()
#Here is where winwen and count helps determine the winner of the 3 board tic tac toe game as they can set the number to the variable "win" and identify who won
        if winwen == 3 and count == 1:
            win = win + 1
        if winwen == 3 and count == 2:
            win = win + 2
        if win == 1 or win == 2:
            if win == 1:
                print("Player X won the last board!!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
#Plop is an input asked after the game has been won, it resets the entire game if the answer to it is "yes"
                if plop == "yes" or plop == "y" or plop == "YES":
                    winwen = 0
                    threebord()
                return True
            if win == 2:
                print("Player O won the last board!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
                if plop == "yes" or plop == "y" or plop == "YES":
                    winwen = 0
                    threebord()
                return True
#In here, for x in range(0,28) or range(28) would've been sufficient but I prefer them seperated for coding conveniency
        for x in range(0,9):
            if board[x] == "X" or board[x] == "O" or board[x] == "-":
                tie = tie + 1
        for x in range(9,18):
            if board[x] == "X" or board[x] == "O" or board[x] == "-":
                tie = tie + 1
        for x in range(18,28):
            if board[x] == "X" or board[x] == "O" or board[x] == "-":
                tie = tie + 1
        if tie == 27 and winwen < 3:
            print("It's a Tie!!")
            plop = input("Do you want to play again? (Type yes)")
            if plop == "yes" or plop == "y" or plop == "YES":
                winwen = 0
                threebord()
            return True
            
#The actual code after the user defined functions
#The code breaks when end is set to true
    print("WELCOME TO THE VARIATION OF 3 BOARD TIC TAC TOE")
    time.sleep(4)
    print("IN THIS VARIATION.... THE LAST BOARD....")
    time.sleep(3)
    print("CAN BE ANY BOARD!!!!! NOT JUST THE RIGHTMOST BOARD!! WOOOH COOL RIGHT?")
    time.sleep(2)
    while end != True:
        blocks()
        print("Player X choose where to place an X")
        playerx()
        print()
        end = ending()
        if end == True:
            return end
        blocks()
        print("Player O choose where to place an O")
        playero()
        print()
        end = ending()
        if end == True:
            return end
        
            
#And this whole project is brought to life by this one line down here <3
threebord()
