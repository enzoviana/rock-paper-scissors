import random

while True:
    print ('rock , paper, Scissors ')
    guest = str(input())
    guest = guest.lower()

    choices = ['rock','paper','scissors']

    computer = random.choice(choices)
    print (computer)

    if computer == guest:
        print ("tie")
    if guest == 'rock':
        if computer == 'paper':
            print ('you lose')
        elif computer == 'scissors':
            print ('you win')
    if guest == 'paper':
        if computer == 'scissors':
            print ('you lose')
        elif computer == 'rock':
            print ('you win')
    if guest == 'scissors':
        if computer == 'rock':
            print ('you lose')
        elif computer == 'paper':
            print ('you win')