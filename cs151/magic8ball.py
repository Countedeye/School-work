import random
import time

def tellYourFortune(whichOne):
    if whichOne == 1:
        print( "As I see it, yes.")
    elif whichOne == 2:
        print("Ask again later.")   
    elif whichOne == 3:
        print("Better not tell you now.")
    elif whichOne == 4:
        print("Cannot predict now.")
    elif whichOne == 5:
        print("Concentrate and ask again.")
    elif whichOne == 6:
        print("Don't count on it.")
    elif whichOne == 7:
        print("It is certain.")
    elif whichOne == 8:
        print("It is decidedly so.")
    else: 
        print("INVALID ENTRY")




#ask if they want to play.
answer= input("Would you like to shake the magic 8 ball for your fortune? ")
#Beginning structured code.
while answer=="y" or answer=="Y" or answer=="yes" or answer=="Yes":
    #ask the user to enter a question.
    userQuestion=input("What question would you like answered? ")
    #Shake the ball three times with one second pause.
    print("SHAKE")
    time.sleep(1)
    print("SHAKE")
    time.sleep(1) 
    print("SHAKE")
    time.sleep(1)      
    #Create a random number between 1 and 8.    
    fortune = random.randint(1,8)
    #pass that random number as the argument.
    tellYourFortune(fortune)
    #ask them if want to play again.
    answer=input("Do you want to shake again for another fortune? ")


'''
These are the 8 responses:
As I see it, yes.
Ask again later.
Better not tell you now.
Cannot predict now.
Concentrate and ask again.
Don't count on it.
It is certain.
It is decidedly so.'''