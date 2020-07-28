# Rock, Paper, Scissors
#
# Automate The Boring Stuff (ATBS) was telling me to make this program,
# by following the book / tutorial to write the source code
# which is already there, NOT to do it on my own.
#
# However, I wanted to challenge myself and try to do it BEFORE seeing the source.
# Initially, I made it to print just what ATBS was saying (rpsGameOwnVersion.py),
# but then I've wanted to take it further, so that I could really play this.
#
# So, I added a computer bot or something like that, so that
# I can play with the computer. The computer is choosing randomly
# (rock, paper or scissors) on his own.
#
# Initially, I've had an extra variable in which I've stored a string based on
# user's choice (e.g. 'ROCK' for 'r') and I also compared the strings such as
# 'r' and 'p' instead 'ROCK' and 'PAPER'. But I got rid of them, thinking that maybe
# it could make the code cleaner or easier to read.
#
# I've used only the knowledge which I've learnt until this point (Chapter 2).
# I've used something which wasn't covered by the book until now though, and that's the slash
# in print (e.g.  print('You don\'t want')   ). I knew that I had to use the slash to
# be able to print with apostrophe, either from the last time I've started to learn
# Python (last year) or from the days when I was doing Android custom ROM development.
#


import random, sys

wins = 0
losses = 0
ties = 0

print('ROCK, PAPER, SCISSORS')

while True:
    # Computer chooses.
    randomChoice = random.randint(1, 3)
    if randomChoice == 1:
        computerMove = 'ROCK'
    elif randomChoice == 2:
        computerMove = 'PAPER'
    elif randomChoice == 3:
        computerMove = 'SCISSORS'

    quit = 0
    print()
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    userMove = input()
    print()

    # If the user doesn't give a valid answer, then ask again.
    while userMove != 'r' and userMove != 'p' and userMove != 's' and userMove != 'q':
        quit = quit + 1

     # Quit the game if the user gives a wrong answer 3 times in row.
        if quit == 3:
            print('You don\'t even wanna play with me...')
            print('I\'m leaving now.')
            sys.exit()

        print('This is not a valid move!')
        userMove = input()
        print()

    # The user's choice result
    if userMove == 'r':
        userMove = 'ROCK'
    elif userMove == 'p':
        userMove = 'PAPER'
    elif userMove == 's':
        userMove = 'SCISSORS'
    elif userMove == 'q' and wins == 0 and losses == 0 and ties == 0:
        print()
        print('We haven\'t even played yet, and you\'re already giving up?')
        print('I won then HAHAHA!')
        sys.exit()
    elif userMove == 'q':
        print()
        print('You\'ve gave up so fast, HAHAHA!')
        sys.exit()

    # Compare your moves to computer's move to see if you win, lose, or it is a tie.
    if userMove == computerMove:
        print(userMove + ' versus...')
        print(computerMove)
        print('It is a tie!')
        ties = ties + 1

    elif userMove == 'ROCK' and computerMove == 'SCISSORS':    # Rock beats Scissors
        print(userMove + ' versus...')
        print(computerMove)
        print('You win!')
        wins = wins + 1

    elif userMove == 'ROCK' and computerMove == 'PAPER':       # Paper beats Rocks
        print(userMove + ' versus...')
        print(computerMove)
        print('You lose!')
        losses = losses + 1

    elif userMove == 'PAPER' and computerMove == 'ROCK':       # Paper beats Rocks
        print(userMove + ' versus...')
        print(computerMove)
        print('You win!')
        wins = wins + 1

    elif userMove == 'PAPER' and computerMove == 'SCISSORS':   # Scissors beats Papers
        print(userMove + ' versus...')
        print(computerMove)
        print('You lose!')
        losses = losses + 1

    elif userMove == 'SCISSORS' and computerMove == 'PAPER':   # Scissors beats Paper
        print(userMove + ' versus...')
        print(computerMove)
        print('You win!')
        wins = wins + 1

    elif userMove == 'SCISSORS' and computerMove == 'ROCK':    # Rock beats Scissors
        print(userMove + ' versus...')
        print(computerMove)
        print('You lose!')
        losses = losses + 1
