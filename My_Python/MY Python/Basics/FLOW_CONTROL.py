#(1)
#print('My name is')
#for i in range(5):
#    print('Jimmy Five Times (' + str(i) + ')')

#(2)
#total = 0
#print('enter rang')
#d =input()
#for num in range(int(d)):
#    total = total + num
#print(total)

#(3)
#for i in range(12,16,3): #for loop upcounting
#    print(i)
#for i in range(5, -1, -1): #for loop downcounting
#    print(i)

#(4)counts from 0 to 2
#for i in range(3): #for loop upcounting
#    print(i)

#(4)
#import random
#for i in range(5):
#    print(random.randint(1, 10))

#(5)
#from random import *
#for i in range(5):
#    print(randint(1, 10))

#(6)
#import sys
#while True:
#    print('Type exit to exit.')
#    response = input()
#    if response == 'exit':
#        sys.exit()
#    print('You typed ' + response + '.')

#(7)
# This is a guess the number game.
#import random
#secretNumber = random.randint(1, 20)
#print('I am thinking of a number between 1 and 20.')
# Ask the player to guess 6 times.
#for guessesTaken in range(1, 7):
#    print('Take a guess.')
#    guess = int(input())
#    if guess < secretNumber:
#        print('Your guess is too low.')
#    elif guess > secretNumber:
#        print('Your guess is too high.')
#    else:
#        break    # This condition is the correct guess!
#if guess == secretNumber:
#    print('Good job! You guessed my number in ' + str(guessesTaken) + 'guesses!')
#else:
#    print('Nope. The number I was thinking of was ' + str(secretNumber))

#(8) ROCK, PAPER, SCISSORS
#import random, sys
#print('ROCK, PAPER, SCISSORS')
## These variables keep track of the number of wins, losses, and ties.
#wins = 0
#losses = 0
#ties = 0
#while True: # The main game loop.
#    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
#    while True: # The player input loop.
#        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
#        playerMove = input()
#        if playerMove == 'q':
#            sys.exit() # Quit the program.
#        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
#            break # Break out of the player input loop.
#        print('Type one of r, p, s, or q.')
#    # Display what the player chose:
#    if playerMove == 'r':
#        print('ROCK versus...')
#    elif playerMove == 'p':
#        print('PAPER versus...')
#    elif playerMove == 's':
#        print('SCISSORS versus...')
#    # Display what the computer chose:
#    randomNumber = random.randint(1, 3)
#    if randomNumber == 1:
#        computerMove = 'r'
#        print('ROCK')
#    elif randomNumber == 2:
#        computerMove = 'p'
#        print('PAPER')
#    elif randomNumber == 3:
#        computerMove = 's'
#        print('SCISSORS')
#    # Display and record the win/loss/tie:
#    if playerMove == computerMove:
#        print('It is a tie!')
#        ties = ties + 1
#    elif playerMove == 'r' and computerMove == 's':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 'p' and computerMove == 'r':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 's' and computerMove == 'p':
#        print('You win!')
#        wins = wins + 1
#    elif playerMove == 'r' and computerMove == 'p':
#        print('You lose!')
#        losses = losses + 1
#    elif playerMove == 'p' and computerMove == 's':
#        print('You lose!')
#        losses = losses + 1
#    elif playerMove == 's' and computerMove == 'r':
#        print('You lose!')
#        losses = losses + 1