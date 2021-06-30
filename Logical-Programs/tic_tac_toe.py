'''
/**********************************************************************************
@Author: Amar Pawar
@Date: 2021-06-30
@Last Modified by: Amar Pawar
@Last Modified time: 2021-06-30
@Title : Play Tic-Tac-Toe game
/**********************************************************************************
'''
import random

# initialise board with range 10 just to add extra space
board = [' ' for i in range(10)]

# to add x or o at particular position
def insert_letter(letter, pos):
    """
    Description:
        This function will insert letter of player or computer at slected position.
    Parameter:
        It takes position of tile and letter of computer or player as parameters.
    """
    board[pos] = letter

# read or check empty tile
def free_space(pos):
    """
    Description:
        This function will check for the free space on board.
    Parameter:
        It takes position of tile as parameter to check for free space.
    Return:
        It returns the free space on the board
    """
    return board[pos] == ' '

# print board of 9x9
def print_board(board):
    """
    Description:
        This function is for printing the board.
    Parameter:
        It takes initialized board as parameter.
    """
    print(board[1] + '|' + board[2] + '|' + board[3])
    print("-------")
    print(board[4] + '|' + board[5] + '|' + board[6])
    print("-------")
    print(board[7] + '|' + board[8] + '|' + board[9])

# main code to execute tic tac toe
def main():
    print_board(board)
    # inside while loop check for when board is not full
    while not (full_board(board)):
        # if user is not winner then computer will play
        if not (winner(board, ('x'))):
            move = computer_move()
            # if no moves left then print  tie game
            if move == 0:
                print("tie")
            else:
                # if not then insert computer move
                insert_letter('o', move)  
                print("computer move: ", move)
            print_board(board)
            # if board is full and no winning condition is satisfied
            if full_board(board):
                print("tie")
                break

        else:
            print("user won")
            break

        if not (winner(board, ('o'))):
            player_move()  # player move
            print_board(board)  # print updated board after player move

        else:
            print("computer won")
            break

        if full_board(board):  # if board is full and no winning condition is satisfied
            print("tie")  # then print tie
       
# take value from tile and store it in common variable      
def winner(b, l):  
    """
    Description:
        This function is to check for all the winning conditions.
    Parameter:
        It takes position of tile and move as parametrs which it stores in vairable
        and checkes if condition is satisfied.
    """
    # winning conditions
    return (b[1] == l and b[2] == l and b[3] == l or
            b[4] == l and b[5] == l and b[6] == l or
            b[7] == l and b[8] == l and b[9] == l or
            b[1] == l and b[4] == l and b[7] == l or
            b[2] == l and b[5] == l and b[8] == l or
            b[3] == l and b[6] == l and b[9] == l or
            b[1] == l and b[5] == l and b[9] == l or
            b[3] == l and b[5] == l and b[7] == l)

def player_move():
    """
    Description:
        This function is for players to play his move by selecting move between 1-9.
        It checks for if free space is available or not and print the player move.
        It also checks for input value is correct or not.
    """
    run = True
    while run:
        # select between 1-9 as board have 9 tiles
        move = input("select between 1-9: ")
        try:
            # converting string value in integer
            move = int(move)
            if 0 < move < 10:
                if free_space(move):
                    run = False
                    # insert x on players move
                    insert_letter('x', move)  
                else:
                    print("this is occupied")

            else:
                print("invalid number")

        except ValueError:
            print("Please type integer value  between 1-9")  # if user enter string value


def computer_move():
    """
    Description:
        This function is for computer to play its move by by random numbers.
        It checks for if free space is available or not and print the computer move.
        It also checks for corner available, winning positions available and
        and according to that computer plays its move.
    """
    possible_move = [x for x, letter in enumerate(board) if letter == ' ' and x != 0]
    move = 0
    # possible letters on board
    for let in ['o', 'x']:
        # possible moves can be empty or 'o'
        for i in possible_move:
            # board[:] copy the board in variable
            board_copy = board[:]
            board_copy[i] = let
            # check winning condition
            if winner(board_copy, let):
                # if move is winning move then select move
                move = i
                return move
    # create corner array which store corner tiles
    corner = []
    for i in possible_move:
        if i in [1, 3, 7, 9]:  # corner tiles
            corner.append(i)  # place computer move of corner tile

    if len(corner) > 0:
        # select random corner tile
        move = select_random(corner) 
        return move
    # if winning tile is middle tile 5 then computer will go for 5
    if 5 in possible_move:
        move = 5
        return move
    # edge array for position 2,4,6,8 tiles
    edge = []
    for i in possible_move:
        if i in [2, 4, 6, 8]:
            edge.append(i)
    # select non empty edge randomly
    if len(edge) > 0:
        move = select_random(edge)
        return move

# select randomly from corner array or edge array and store array in li
def select_random(li):
    """
    Description:
        This function generates random number for computer move according to conditions.
    Parameter:
        It takes list as parameter according to it generates random number.
    Return:
        It returns the random number for computer move
    """
    ln = len(li)
    r = random.randrange(0, ln)
    return li[r]


def full_board(board):  # check whether all tiles are occupied
    """
    Description:
        This function checks for if board is full or not.
    Parameter:
        It takes initialized board as parameter.
    Return:
        It returns the boolean value true or false
    """
    # if any of the tile is empty then board is not full
    if board.count(' ') > 1:
        return False
    else:
        return True

main()