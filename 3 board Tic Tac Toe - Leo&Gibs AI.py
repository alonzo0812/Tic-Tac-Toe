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

#References for this version
# How to randomly generate integers - https://stackoverflow.com/questions/3996904/generate-random-integers-between-0-and-9

#Although one of the issues in this version is that since the computer chooses random integers it can sometimes endlessly spam a taken integer until it
#chooses a proper board number


#For time.sleep between prints on the introduction
import time
import random #for the computer's moves
#IN THIS VERSION YOU CAN OPT TO FIGHT A BASIC AI OR AN ADVANCED AI
def threebord():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    end = False
    win1 = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win2 = ((10, 11, 12), (13, 14, 15), (16, 17, 18), (10, 13, 16), (11, 14, 17), (12, 15, 18), (10, 14, 18), (12, 14, 16))
    win3 = ((19, 20, 21), (22, 23, 24), (25, 26, 27), (19, 22, 25), (20, 23, 26), (21, 24, 27), (19, 23, 27), (21, 23, 25))
    def blocks():
        print(board[0], board[1], board[2], "       ", board[10], board[11], board[12], "       ", board[19], board[20], board[21])
        print(board[3], board[4], board[5], "       ", board[13], board[14], board[15], "       ", board[22], board[23], board[24])
        print(board[6], board[7], board[8], "       ", board[16], board[17], board[18], "       ", board[25], board[26], board[27])
        print()
    def number():
        while True:
                x = input()
                try:
                    x  = int(x)
                    x = x - 1
                    if x in range(0, 28):
                        return x
                    else:
                        print("That's not on the board")
                        plop = number()
                        return plop
                except ValueError:
                   print("That's not a number")
                   plop = number()
                   return plop
    def playerx():
        n = number()
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playerx()
        else:
            board[n] = "X"
#For the basic version I just have to change the script of the user defined function playero()
    def playero():
        n = random.randint(0,27)
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playero()
        else:
            board[n] = "O"

    def ending():
        tie = 0
        win = 0
        for x in win1:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the first board!")
                board[0] = "-"
                board[1] = "-"
                board[2] = "-"
                board[3] = "-"
                board[4] = "-"
                board[5] = "-"
                board[6] = "-"
                board[7] = "-"
                board[8] = "-"
                blocks()
                print("Player X gets an extra turn! choose where to place an O")
                playerx()
                print()
                ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("BASIC AI won the first board!")
                board[1] = "-"
                board[2] = "-"
                board[3] = "-"
                board[4] = "-"
                board[5] = "-"
                board[6] = "-"
                board[7] = "-"
                board[8] = "-"
                blocks()
                print("BASIC AI gets an extra turn! choose where to place an O")
                playero()
                print()
                ending()
        for x in win2:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the second board!")
                board[10] = "-"
                board[11] = "-"
                board[12] = "-"
                board[13] = "-"
                board[14] = "-"
                board[15] = "-"
                board[16] = "-"
                board[17] = "-"
                board[18] = "-"
                blocks()
                print("Player X gets an extra turn! choose where to place an X")
                playerx()
                print()
                ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("BASIC AI won the second board!")
                board[10] = "-"
                board[11] = "-"
                board[12] = "-"
                board[13] = "-"
                board[14] = "-"
                board[15] = "-"
                board[16] = "-"
                board[17] = "-"
                board[18] = "-"
                blocks()
                print("BASIC AI gets an extra turn! choose where to place an O")
                playero()
                print()
                ending()
        for x in win3:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the third board!")
                board[19] = "-"
                board[20] = "-"
                board[21] = "-"
                board[22] = "-"
                board[23] = "-"
                board[24] = "-"
                board[25] = "-"
                board[26] = "-"
                board[27] = "-"
                print("Player X won the last board!!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
                if plop == "yes" or plop == "y" or plop == "YES":
                    threebord()
                return True
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("BASIC AI won the third board!")
                board[19] = "-"
                board[20] = "-"
                board[21] = "-"
                board[22] = "-"
                board[23] = "-"
                board[24] = "-"
                board[25] = "-"
                board[26] = "-"
                board[27] = "-"
                print("BASIC AI won the last board!!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
                if plop == "yes" or plop == "y" or plop == "YES":
                    threebord()
        for x in range(19,28):
            if board[x] == "X" or board[x] == "O" or board[x] == "-":
                tie = tie + 1
        if tie == 9:
            print("It's a Tie!!")
            plop = input("Do you want to play again? (Type yes)")
            if plop == "yes" or plop == "y" or plop == "YES":
                threebord()
            return True
            
    while end != True:
        blocks()
        print("Player X choose where to place an X")
        playerx()
        print()
        end = ending()
        if end == True:
            return end
        blocks()
        print("BASIC AI is choosing where to place an O")
        playero()
        print()
        end = ending()
        if end == True:
            return end
def threebordadvanced():
    board = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28]
    end = False
    win1 = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
    win2 = ((10, 11, 12), (13, 14, 15), (16, 17, 18), (10, 13, 16), (11, 14, 17), (12, 15, 18), (10, 14, 18), (12, 14, 16))
    win3 = ((19, 20, 21), (22, 23, 24), (25, 26, 27), (19, 22, 25), (20, 23, 26), (21, 24, 27), (19, 23, 27), (21, 23, 25))
    def blocks():
        print(board[0], board[1], board[2], "       ", board[10], board[11], board[12], "       ", board[19], board[20], board[21])
        print(board[3], board[4], board[5], "       ", board[13], board[14], board[15], "       ", board[22], board[23], board[24])
        print(board[6], board[7], board[8], "       ", board[16], board[17], board[18], "       ", board[25], board[26], board[27])
        print()
    def number():
        while True:
                x = input()
                try:
                    x  = int(x)
                    x = x - 1
                    if x in range(0, 28):
                        return x
                    else:
                        print("That's not on the board")
                        plop = number()
                        return plop
                except ValueError:
                   print("That's not a number")
                   plop = number()
                   return plop
    def playerx():
        n = number()
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playerx()
        else:
            board[n] = "X"
#I'll be honest the advanced version just places on the last board other than the basic one which places on any of the boards
#Because seriously.. always moving on the rightmost board is just 1000000x better than moving on the first two
    def playero():
        n = random.randint(19,27)
        if board[n] == "X" or board[n] == "O" or board[n] == "-":
            print("You can't go there")
            playero()
        else:
            board[n] = "O"

    def ending():
        tie = 0
        win = 0
        for x in win1:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the first board!")
                board[0] = "-"
                board[1] = "-"
                board[2] = "-"
                board[3] = "-"
                board[4] = "-"
                board[5] = "-"
                board[6] = "-"
                board[7] = "-"
                board[8] = "-"
                blocks()
                print("Player X gets an extra turn! choose where to place an O")
                playerx()
                print()
                ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("ADVANCED AI won the first board!")
                board[1] = "-"
                board[2] = "-"
                board[3] = "-"
                board[4] = "-"
                board[5] = "-"
                board[6] = "-"
                board[7] = "-"
                board[8] = "-"
                blocks()
                print("ADVANCED AI gets an extra turn! choose where to place an O")
                playero()
                print()
                ending()
        for x in win2:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the second board!")
                board[10] = "-"
                board[11] = "-"
                board[12] = "-"
                board[13] = "-"
                board[14] = "-"
                board[15] = "-"
                board[16] = "-"
                board[17] = "-"
                board[18] = "-"
                blocks()
                print("Player X gets an extra turn! choose where to place an X")
                playerx()
                print()
                ending()
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("ADVANCED AI won the second board!")
                board[10] = "-"
                board[11] = "-"
                board[12] = "-"
                board[13] = "-"
                board[14] = "-"
                board[15] = "-"
                board[16] = "-"
                board[17] = "-"
                board[18] = "-"
                blocks()
                print("ADVANCED AI gets an extra turn! choose where to place an O")
                playero()
                print()
                ending()
        for x in win3:
            if board[x[0]] == board[x[1]] == board[x[2]] == "X":
                print("Player X won the third board!")
                board[19] = "-"
                board[20] = "-"
                board[21] = "-"
                board[22] = "-"
                board[23] = "-"
                board[24] = "-"
                board[25] = "-"
                board[26] = "-"
                board[27] = "-"
                print("Player X won the last board!!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
                if plop == "yes" or plop == "y" or plop == "YES":
                    threebordadvanced()
                return True
            if board[x[0]] == board[x[1]] == board[x[2]] == "O":
                print("ADVANCED AI won the third board!")
                board[19] = "-"
                board[20] = "-"
                board[21] = "-"
                board[22] = "-"
                board[23] = "-"
                board[24] = "-"
                board[25] = "-"
                board[26] = "-"
                board[27] = "-"
                print("ADVANCED AI won the last board!!!!! woo!!")
                plop = input("Do you want to play again? (Type yes)")
                if plop == "yes" or plop == "y" or plop == "YES":
                    threebordadvanced()
        for x in range(19,28):
            if board[x] == "X" or board[x] == "O" or board[x] == "-":
                tie = tie + 1
        if tie == 9:
            print("It's a Tie!!")
            plop = input("Do you want to play again? (Type yes)")
            if plop == "yes" or plop == "y" or plop == "YES":
                threebordadvanced()
            return True
            
    while end != True:
        blocks()
        print("Player X choose where to place an X")
        playerx()
        print()
        end = ending()
        if end == True:
            return end
        blocks()
        print("ADVANCED AI is choosing where to place an O")
        playero()
        print()
        end = ending()
        if end == True:
            return end
        
print("HEY GUYS WELCOME TO ADVANCED OR SIMPLE AI 3 BOARD TIC TAC TOE")
time.sleep(4)
print("IN HERE YOU CAN OPT TO PLAY AN ADVANCED OR BASIC AI LETS GO!!")
time.sleep(3)
blopopz = input("Type Basic to fight the BASIC AI and type Advanced to fight the ADVANCED AI")
if blopopz == "Basic" or blopopz == "basic" or blopopz == "BASIC":
    threebord()
elif blopopz == "Advanced" or blopopz == "advanced" or blopopz == "ADVANCED":
    threebordadvanced()

