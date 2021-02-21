import random #import the random class
import time #import the time class.



#define function
def determineWinner(winsPlayer1, winsPlayer2):
    if (winsPlayer1 < winsPlayer2):
        print("Since the game favored Player two " + str(winsPlayer2) + " to " + str(winsPlayer1))
        print("Player Two wins!")
    elif (winsPlayer1 > winsPlayer2):
        print("Since the game favored Player one " + str(winsPlayer1) + " to " + str(winsPlayer2))
        print("Player one wins!")
    else:
        print("Its a draw.")
        
    
    
    #Introduce how the game will be played
print("This is a Game of War...")
time.sleep(2) 
print("between two players trying to be crowned Champion!")
time.sleep(2)
print("The game will be best of 10...")
time.sleep(2)
answer = input("Are you ready for the showdown? ")
while answer =='y'or answer =='Y' or answer == 'Yes' or answer == 'yes':    
    #This was the trickiest part of the code. I couldnt get it to keep count due to this being in my "for loop". After debugging this works.
    player1 = int(0)
    player2 = int(0)
    #Play 10 rounds
    for i in range(10):
        card1 = random.randint(1, 10)
        card2 = random.randint(1, 10)
        #Each round, display the card that player 1 drew, and the card player 2 drew
        print (str("Player One: "+str(card1)))
        print (str("Player Two: "+str(card2)))
        #At the end of each round, display the final scores, and display who won.
        if card1 > card2:
            print("Player One wins! ")
            player1 += 1
        elif card1 < card2:
            print("Player Two wins! ")
            player2 += 1
        else:
            print("Draw.")
        #Wait 2 seconds between rounds
        time.sleep(2)   
    determineWinner(player1,player2)
    answer = input("Do you want to watch again?")