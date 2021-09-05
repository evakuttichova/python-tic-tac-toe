import numpy as np 
import random

from numpy.lib.function_base import append 
random.seed(1)

#Creates tboard

def create_board():
    board = np.zeros((3,3), dtype=int)
    return board

board = create_board()

print("Your board has been created:")
print(board)

#Place 1 or 2

def place(board, player, position):
    if player == 1 and board[position] == 0:
        board[position] = 1
    elif player == 2 and board[position] == 0: 
        board[position] = 2
    else:
        print("Error")
    return board

#Creates two arrays with free coordinates

def possibilities(board):
    possitions_x = np.empty(0, dtype=int)
    possitions_y = np.empty(0, dtype=int)
    x = 0
    y = 0
    for x in range(3):
        y = 0
        for y in range(3):
            if board[x, y] == 0:
                possitions_x = np.append(possitions_x, x)
                possitions_y = np.append(possitions_y, y)
            y += 1 
        x += 1
    return possitions_x, possitions_y

#Generates random possition

def random_place(board):
    results = possibilities(board)
    possitions_x = results[0]
    possitions_y = results[1]
    i = np.random.randint(0,len(possitions_x))
    random_possition = (possitions_x[i], possitions_y[i])
    return random_possition

#Player randomly place

def player_place(player):
    coordinates = random_place(board) 
    place(board, player, coordinates)

#Player move

def player_move(player, board):
    if possibilities(board) != None:
        player_place(player)
        if row_win(board) != None or col_win(board) != None or diag_win(board) != None:
            print("Player " + str(player) + " is winner!")  
    else:
        print("Game Over!")      

#Check if player win

def row_win(board):
    for i in range(2):
        if board[i, 0] == board[i, 1] and board[i, 1] == board[i, 2] and board[i, 0] != 0:
            return True

def col_win(board):
    for i in range(2):
        if board[0, i] == board[1, i] and board[1, i] == board[2, i] and board[0, i] != 0:
            return True

def diag_win(board):
        if board[0, 0] == board[1, 1] and board[1, 1] == board[2, 2] and board[0, 0] != 0 and board[2, 0] != 0:
            return True
        elif board[2, 0] == board[1, 1] and board[1, 1] == board[0, 2] and board[0, 0] != 0 and board[2, 0] != 0:
            return True


#Game play

for i in range(4):
    print("Round: " + str(i))
    player_move(1, board)
    if row_win(board) != None or col_win(board) != None or diag_win(board) != None:
        print(board)
        break    
    player_move(2, board)
    if row_win(board) != None or col_win(board) != None or diag_win(board) != None:
        print(board)
        break   
    print(board) 
    

    

