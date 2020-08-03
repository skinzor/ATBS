import sys


def userTurn(gameBoard, player1):

    move = input('\n')
    print()

    # Check if the user's move is valid.
    if move == 'top-L' or move == 'top-M' or move == 'top-R'\
       or move == 'mid-L' or move == 'mid-M' or move == 'mid-R'\
       or move == 'low-L' or move == 'low-M' or move == 'low-R':
        # Check whether the slot is already occupied or not. If it is, then ask for a new move.
        if gameBoard[move] == ' ':
            gameBoard[move] = player1
        else:
            print('That slot is already occupied! Try again!')
            userTurn(gameBoard, player1)
    else:
        print('This isn\'t a valid move! Only those are allowed:\n')
        userTurn(gameBoard, player1)   # User must type the move again and make sure that's a proper one.


def userWin():
    global userWon
    userWon = 1
    print('\nYou won! Game over!')
    sys.exit()


def check_user_win(gameBoard, player1):
    
    # Rows possible wins
    if gameBoard['top-L'] == player1 and gameBoard['top-M'] == player1 and gameBoard['top-R'] == player1:
        userWin()

    elif gameBoard['mid-L'] == player1 and gameBoard['mid-M'] == player1 and gameBoard['mid-R'] == player1:
        userWin()

    elif gameBoard['low-L'] == player1 and gameBoard['low-M'] == player1 and gameBoard['low-R'] == player1:
        userWin()


    # Columns possible wins
    elif gameBoard['top-L'] == player1 and gameBoard['mid-L'] == player1 and gameBoard['low-L'] == player1:
        userWin()

    elif gameBoard['top-M'] == player1 and gameBoard['mid-M'] == player1 and gameBoard['low-M'] == player1:
        userWin()
    
    elif gameBoard['top-R'] == player1 and gameBoard['mid-R'] == player1 and gameBoard['low-R'] == player1:
        userWin()


    # Diagonal possible wins
    elif gameBoard['top-L'] == player1 and gameBoard['mid-M'] == player1 and gameBoard['low-R'] == player1:
        userWin()

    elif gameBoard['top-R'] == player1 and gameBoard['mid-M'] == player1 and gameBoard['low-L'] == player1:
        userWin()

    # If didn't win
    elif ' ' not in gameBoard.values():
        return 'no'
