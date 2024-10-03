# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Alex So
#               Garret Sumpter
#               Zane Aschenback
#               Clint Smith
# Section:      573
# Assignment:   Unit 7 Team Lab
# Date:         10-1-24
#

#prints the current board
def printBoard(board):
    for i in range(9):
        for j in range(9):
            print(f'{board[i][j]} ', end='')
        print()

#board initialization
board = []
for i in range(9):
    line = []
    for j in range(9):
        line.append('.')
    board.append(line)

#game pieces
bStone = chr(9679)
wStone = chr(9675)

action = ''
#True means white turn, false means black turn
turn = True
#whether to skip the board display
skip = False

#game logic
while(True):

    if(not skip):
        printBoard(board)
    skip = False

    #determines turn and asks for move
    if(turn):
        turn = False
        action = input("White to move: ")
    else:
        turn = True
        action = input("Black to move: ")

    #checks for stop
    if(action.lower() == 'stop'):
        break
    
    #determines move coordinates
    move = action.split()

    #attempts to place piece in user given location, printing invalid if an error occurs (meaning invalid move)
    try:
        x = int(move[0])
        y = int(move[1])
        #throws an exception if the user tries to place a piece in an already occupied location
        if(board[x][y] != '.' or x < 0 or y < 0):
            raise Exception()
        board[x][y] = wStone if turn else bStone
    except:
        print('Invalid move.')
        skip = True
        turn = not turn
   
        
    