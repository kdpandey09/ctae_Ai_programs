# Program by KDPandey09
import random

board = ["-","-","-","-","-","-","-","-","-"]

#global variables
playing_game = True
winner  = None
current_player = "X"

#creating board
def display_board(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


#player input
def player_input(board):
    pos = int(input("choose spot 1-9 :- "))
    if board[pos-1] == "-":
        board[pos-1] = current_player
    else:
        print("player is already at that spot.")


#winning conditions
#checking rows
def check_rows(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True

#checking column
def check_column(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

#checking diagonals
def check_diag(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[4] != "-":
        winner = board[2]
        return True

#checking winner
def check_win(board):
    global playing_game
    if check_rows(board):
        display_board(board)
        print(f"The winner is {winner}")
        playing_game = False

    elif check_column(board):
        display_board(board)
        print(f"The winner is {winner}")
        playing_game = False

    elif check_diag(board):
        display_board(board)
        print(f"The winner is {winner}")
        playing_game = False


#checking game is tie or not
def check_tie(board):
    global playing_game
    if "-" not in board:
        display_board(board)
        print("It is a tie!")
        playing_game = False


#switch player
def flip_player():
    global current_player
    if current_player == "X":
        current_player = "O"
    else:
        current_player = "X"

print("         Tic-Tac-Toe Game AI         ")
while playing_game:
    display_board(board)
    player_input(board)
    check_win(board)
    check_tie(board)
    flip_player()
