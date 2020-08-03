# I was reading Automate The Boring Stuff and I was at
# Chapter 5 (well, still am as of typing this, after I
# kinda finished this program).
#
# I got to the section "A Tic-Tac-Toe Board" and again,
# I didn't scroll beyond the sentence which told me to
# open a file editor to write the source code for this
# program.
#
# I stopped there and I started to make this program.
#
# After I finished this, I took a look at the Chapter
# to see what source code it was telling me to write.
#
# And I was surprised to see that it wasn't actually a
# complete tic-tac-toe game that I was supposed to
# write.
#
# I wrote this using the knowlege I've learn since the
# first chapter. However, I believe I forgot some
# things and it could be done in a much simpler and
# cleaner way. I have no doubts about that.
#


import userMoves, computerMoves, time, random, sys


gameBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
             'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
             'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def createBoard():
    print(gameBoard['top-L'] + '|' + gameBoard['top-M'] + '|' + gameBoard['top-R'])
    print(gameBoard['mid-L'] + '|' + gameBoard['mid-M'] + '|' + gameBoard['mid-R'])
    print(gameBoard['low-L'] + '|' + gameBoard['low-M'] + '|' + gameBoard['low-R'])


def userFirst(gameBoard, player1, player2):

    userMoves.userTurn(gameBoard, player1)
    print()
    createBoard()
    userMoves.check_user_win(gameBoard, player1)

    if ' ' in gameBoard.values() and userWon == 0 :    # if there's still an empty space where a move can be done and if user didn't win yet
        # Computer's turn
        time.sleep(1)
        computerMoves.computerTurn(gameBoard, player2)    # computer make his move
        print()
        createBoard()    # update the board
        computerMoves.check_computer_win(gameBoard, player2)    # check if computer won

    elif userMoves.check_user_win(gameBoard, player1) == 'no' and computerMoves.check_computer_win(gameBoard, player2) == 'no':    # if neither the user and the player won
        print('\nNobody won. It\'s a tie!')
        sys.exit()


def computerFirst(gameBoard, player1, player2):

    time.sleep(1)
    computerMoves.computerTurn(gameBoard, player2)    # Computer make his move
    print()
    createBoard()    # update the board
    computerMoves.check_computer_win(gameBoard, player2)     # check if computer won

    if ' ' in gameBoard.values() and computerWon == 0 :    # if there's still an empty space where a move can be done and if computer didn't win yet
        # User's turn.
        userMoves.userTurn(gameBoard, player1)    # user make his move
        print()
        createBoard()    # update the board
        userMoves.check_user_win(gameBoard, player1)    # check if user won

    elif userMoves.check_user_win(gameBoard, player1) == 'no' and computerMoves.check_computer_win(gameBoard, player2) == 'no':    # if neither the user and the player won
        print('\nNobody won. It\'s a tie!')
        sys.exit()


# Welcome
print()
print('-----------------------')
print('Welcome to Tic Tac Toe!')
print('-----------------------')
print('\n\n')

time.sleep(1)
print('Those are the possible moves. Make sure to remember them!\n\b')
time.sleep(1)
print('top-L   ' + 'top-M   ' + 'top-R'
      '\nmid-L   ' + 'mid-M   ' + 'mid-R'
      '\nlow-L   ' + 'low-M   ' + 'low-R')
print('\n\n')
time.sleep(3)


userWon = 0
computerWon = 0

# Decide who's gonna start first. Player1 is the user, player2 is the computer.
randomTurn = random.randint(0,1)
print('Hmmmm, who should start first?\n')
time.sleep(2)

if randomTurn == 0:
    player1 = 'X'
    player2 = 'O'
    print('You!\n\n')
else:
    player1 = 'O'
    player2 = 'X'
    print('The computer!\n\n')


time.sleep(1)
createBoard()    # create the initial board


for i in range(len(gameBoard)):

    if player1 == 'X':
        # User starts first.
        userFirst(gameBoard, player1, player2)

    elif player2 == 'X':
        # Computer starts first.
        computerFirst(gameBoard, player1, player2)
