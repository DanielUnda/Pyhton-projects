import random
import re
import sys

while (1<2):
    print('\n')
    print("Rock, Paper, Scissor - Shoot!")

    # User input
    userChoice=input("Choose your weapon [R]ock, [P]aper, [S]cissors, [E]xit: ").lower()

    #Validating the user input
    if  (not re.match("[srpe]", userChoice)) or (len(userChoice)!=1):
        print("Please choose a letter: ")
        print("[R]ock, [P]aper, [S]cissors, [E]xit: ")
        continue

    #Show user input
    print(f'You chose: {userChoice}')

    #check if user wants to exit
    if userChoice == 'e':
        print('Exiting Game...')
        break
    
    #Possible choices
    choices=['r','p','s']

    #generating computer's choice
    opponentChoice=random.choice(choices)

    #Show computer choice
    print(f'I chose: {opponentChoice}')

    #check winner
    if userChoice == opponentChoice:
        print('It is a TIE !')
    elif opponentChoice == 'r' and userChoice == 's':            # Rock Vs Scissor - Rock/computer Wins
        print ("Scissors beats rock, I win! ")
        continue
    elif opponentChoice == 's' and userChoice == 'p':            # Scissor Vs Paper - Paper/computer Wins
        print ("Scissors beats paper! I win! ")
        continue
    elif opponentChoice == 'p' and userChoice == 'r':            # Paper Vs Rock - Paper/computer Wins
        print ("Paper beat rock, I win! ")
        continue
    else:                                                                 # In all the other cases, user wins!
        print ("You win!")