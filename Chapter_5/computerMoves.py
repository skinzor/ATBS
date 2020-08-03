import random, sys


def computerTurn(gameBoard, player2):

    # Computer picks a random move
    computerMove = random.randint(0, len(gameBoard) -1)

    if computerMove == 0:
        computerMove = 'top-L'

    elif computerMove == 1:
        computerMove = 'top-M'

    elif computerMove == 2:
        computerMove = 'top-R'

    elif computerMove == 3:
        computerMove = 'mid-L'

    elif computerMove == 4:
        computerMove = 'mid-M'

    elif computerMove == 5:
        computerMove = 'mid-R'

    elif computerMove == 6:
        computerMove = 'low-L'

    elif computerMove == 7:
        computerMove = 'low-M'

    elif computerMove == 8:
        computerMove = 'low-R'

    if gameBoard[computerMove] == ' ':
        gameBoard[computerMove] = player2
    else:    # if that move is already occupied, then computer should try to get a new one
        computerTurn(gameBoard, player2)


def computerWin():
    global computerWon
    computerWon = 1
    print('\nYou lost! Game over!')
    sys.exit()


def check_computer_win(gameBoard, player2):

    # Rows possible wins
    if gameBoard['top-L'] == player2 and gameBoard['top-M'] == player2 and gameBoard['top-R'] == player2:
        computerWin()

    elif gameBoard['mid-L'] == player2 and gameBoard['mid-M'] == player2 and gameBoard['mid-R'] == player2:
        computerWin()

    elif gameBoard['low-L'] == player2 and gameBoard['low-M'] == player2 and gameBoard['low-R'] == player2:
        computerWin()


    # Columns possible wins
    elif gameBoard['top-L'] == player2 and gameBoard['mid-L'] == player2 and gameBoard['low-L'] == player2:
        computerWin()

    elif gameBoard['top-M'] == player2 and gameBoard['mid-M'] == player2 and gameBoard['low-M'] == player2:
        computerWin()

    elif gameBoard['top-R'] == player2 and gameBoard['mid-R'] == player2 and gameBoard['low-R'] == player2:
        computerWin()


    # Diagonal possible wins
    elif gameBoard['top-L'] == player2 and gameBoard['mid-M'] == player2 and gameBoard['low-R'] == player2:
        computerWin()

    elif gameBoard['top-R'] == player2 and gameBoard['mid-M'] == player2 and gameBoard['low-L'] == player2:
        computerWin()

    # If didn't win
    elif ' ' not in gameBoard.values():
        return 'no'
