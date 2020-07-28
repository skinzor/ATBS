# Rock, Paper, Scissors
#
# Automate The Boring Stuff is telling me to make this program,
# by following the book / tutorial to write the source code
# which is already listed.
#
# However, I wanted to try to do it myself BEFORE seeing the source.
#
#
# ATBS says that the program is supposed to output this:
#
#
# ROCK, PAPER, SCISSORS
# 0 Wins, 0 Losses, 0 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# p
# PAPER versus...
# PAPER
# It is a tie!
# 0 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# s
# SCISSORS versus...
# PAPER
# You win!
# 1 Wins, 1 Losses, 1 Ties
# Enter your move: (r)ock (p)aper (s)cissors or (q)uit
# q
#
#
#
# UPDATE: After I've made my rpsGameOwnV2.py, I've checked
# the ATBS source code and it looks like this program wasn't
# supposed to print only the above output with that specific
# user input. Well, nevermind, since my rpsGameOwnV2.py covers that.
#

print('ROCK, PAPER, SCISSORS')

while True:
    print(str(wins) + ' Wins, ' + str(losses) + ' Losses, ' + str(ties) + ' Ties')
    print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
    move = input()

    if move == 'p':
        print('PAPER versus...')
        print('PAPER')
        print('It is a tie!')
        losses = losses + 1
        ties = ties + 1
    elif move == 's':
        print('SCISSORS versus...')
        print('PAPER')
        print('You win!')
        wins = wins + 1
    elif move == 'q':
        break
    
