import random
num=random.randint(1,100)
userchoice=''
while userchoice != 'y':
    print("My computer has chosen a random number! Would you like to quess? Press 1 for unlimited guesses and 2 for only 5 guesses!")
    userinput= input()
    if int(userinput)==1:
        print("what is the number you guess?")
        userguess=input()
        while int(userguess) != int(num):    
            print("Nope Keep Guessing!Pick another number")
            userguess=input()


    elif int(userinput)==2:
        print("You only have 5 guesses good luck! Pick a number.")
        userguess=input()
        for i in range(4):
            if int(userguess) == int(num):
                print("WOW! Congrats!")
                break
            value =4-i
            print("Nope! Only "+ str(value) +" guess left!")
            userguess=input()
    else:  
        print("invalid entry")            