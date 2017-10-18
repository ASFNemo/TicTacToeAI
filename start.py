from sys import exit
from random import randint
from board import Board, PLAYER1, PLAYER2


def PLAYER1ize_coord(coord):
    if coord == PLAYER1:
        return 'O'
    elif coord == PLAYER2:
        return 'X'
    else:
        return ' '

def print_board(board):
    for x in range(board.max_width):
        print "-------------------------------"
        print "|         |         |         |"
        print "|    %s    |    %s    |    %s    |" % \
            (PLAYER1ize_coord(board.board[x][0]), PLAYER1ize_coord(board.board[x][1]), PLAYER1ize_coord(board.board[x][2]))
        print "|         |         |         |"
    print "-------------------------------"

print "============================================================"
print "  Tic Tac Toe - yep, another implementation of this game.   "
print "============================================================"
print

number = None
while not number in ["1", "2", "0"]:
    print "Choose who should start the game first?"
    print
    print "              1) You"
    print "              2) Super PLAYER2"
    print
    print "              0) Exit game, but return later"
    print
    if number == None:
        number = raw_input("Enter number. But choose wisely - all hopes in you: ")
    else:
        number = raw_input("Oops, I have said that only numbers are allowed: ")
    print

board = Board()

if number == "1":
    print "Ok, you will start the game first! Prepare for action!"
    print
    board.player_starts(PLAYER1)
    print_board(board)
elif number == "2":
    print "Super PLAYER2 starts the game. He's thinking about first his move, so"
    print "you should be patient..."
    print
    board.player_starts(PLAYER2)
    board.put(randint(0, 2), randint(0, 2), PLAYER2)
    print_board(board)
else:
    exit(0)

while board.get_winner() == None:
    print
    if board.player_turn() == PLAYER1:
        x = int(raw_input("Now is your turn. Enter X coord starting from 0 to 2: "))
        y = int(raw_input("                  Enter Y coord starting from 0 to 2: "))
        print
        while x not in [0, 1, 2] or y not in [0, 1, 2] or not board.can_put(x, y):
            first = False
            if x not in [0, 1, 2] or y not in [0, 1, 2]:
                print "Oops, invalid coords. Please try again."
            else:
                print "As you can see, this is reserved place. Choose another one!"
            print
            x = int(raw_input("Enter X coord starting from 0 to 2: "))
            y = int(raw_input("Enter Y coord starting from 0 to 2: "))
            print
    else:
        print "PLAYER2 thinking... Oh, here it is:"
        print
        move = board.get_best_move()
        x = move[0]
        y = move[1]

    board.put(x, y, board.player_turn())
    print_board(board)

print
if board.get_winner() == PLAYER2:
    print "Yep, you can't win against Super PLAYER2. But you can try..."
elif board.get_winner() == PLAYER1:
    print "Impossible! You won against the Super PLAYER2! Congrats!"
else:
    print "Well, next time maybe, next time..."

print
raw_input("Game ended, hope you will return back for more. Press ENTER to close...")from sys import exit
from random import randint
from board import Board, PLAYER1, PLAYER2


def PLAYER1ize_coord(coord):
    if coord == PLAYER1:
        return 'O'
    elif coord == PLAYER2:
        return 'X'
    else:
        return ' '

def print_board(board):
    for x in range(board.max_width):
        print "-------------------------------"
        print "|         |         |         |"
        print "|    %s    |    %s    |    %s    |" % \
            (PLAYER1ize_coord(board.board[x][0]), PLAYER1ize_coord(board.board[x][1]), PLAYER1ize_coord(board.board[x][2]))
        print "|         |         |         |"
    print "-------------------------------"

print "============================================================"
print "  Tic Tac Toe - yep, another implementation of this game.   "
print "============================================================"
print

number = None
while not number in ["1", "2", "0"]:
    print "Choose who should start the game first?"
    print
    print "              1) You"
    print "              2) Super PLAYER2"
    print
    print "              0) Exit game, but return later"
    print
    if number == None:
        number = raw_input("Enter number. But choose wisely - all hopes in you: ")
    else:
        number = raw_input("Oops, I have said that only numbers are allowed: ")
    print

board = Board()

if number == "1":
    print "Ok, you will start the game first! Prepare for action!"
    print
    board.player_starts(PLAYER1)
    print_board(board)
elif number == "2":
    print "Super PLAYER2 starts the game. He's thinking about first his move, so"
    print "you should be patient..."
    print
    board.player_starts(PLAYER2)
    board.put(randint(0, 2), randint(0, 2), PLAYER2)
    print_board(board)
else:
    exit(0)

while board.get_winner() == None:
    print
    if board.player_turn() == PLAYER1:
        x = int(raw_input("Now is your turn. Enter X coord starting from 0 to 2: "))
        y = int(raw_input("                  Enter Y coord starting from 0 to 2: "))
        print
        while x not in [0, 1, 2] or y not in [0, 1, 2] or not board.can_put(x, y):
            first = False
            if x not in [0, 1, 2] or y not in [0, 1, 2]:
                print "Oops, invalid coords. Please try again."
            else:
                print "As you can see, this is reserved place. Choose another one!"
            print
            x = int(raw_input("Enter X coord starting from 0 to 2: "))
            y = int(raw_input("Enter Y coord starting from 0 to 2: "))
            print
    else:
        print "PLAYER2 thinking... Oh, here it is:"
        print
        move = board.get_best_move()
        x = move[0]
        y = move[1]

    board.put(x, y, board.player_turn())
    print_board(board)

print
if board.get_winner() == PLAYER2:
    print "Yep, you can't win against Super PLAYER2. But you can try..."
elif board.get_winner() == PLAYER1:
    print "Impossible! You won against the Super PLAYER2! Congrats!"
else:
    print "Well, next time maybe, next time..."

print
raw_input("Game ended, hope you will return back for more. Press ENTER to close...")