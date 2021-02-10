import random
gamechoice = ''
while gamechoice != 'y':
    print("Which program would you like to run? 1 for pyramid, 2 for game of war, and 3 for multiplication facts.")
    userinput=input()
    if int(userinput)==1:
    #pyramid part 1
        num=0
        print("how big do you want your pyramid?")
        userinput= input()
        print("what character do you want for your pyramid?")
        character = input()
        pyramid = character
        while num<int(userinput):
            print(pyramid)
            pyramid = pyramid + character
            num += 1


    elif int(userinput)==2:
    #Game of war part 2
        print("Do you want to play a game of war?")
        initialinput=input()
        while initialinput=='y':
            rand1=random.randint(0,100)
            rand2=random.randint(0,100)
            print(str("Player One:"+str(rand1)))
            print(str("Player Two:"+str(rand2)))
            if (rand1 < rand2):
                print("Player 2 wins!")
            elif rand1>rand2:
                print("Player 1 wins!")
            else:
                print("It's a tie!")
            print("Do you want to play again?")
            initialinput = input()
            


    elif int(userinput) ==3:
    # multiplication part 3 of HW
        print("Do you want to learn some multiplication facts?")
        initialinput = input()
        while initialinput == 'y':
            print("what number would you like to see?")
            inputnum = input()
            num = 0 
            while num < 13:
                total = int(num) * int(inputnum)
                print(str(inputnum) + '*' + str(num) + '=' + str(total))
                num += 1
            print("Do you want to learn some more?")
            initialinput = input()

    else:
        print("invalid entry.")
print("Do you want to play another program?")
gamechoice = input()            


''' I added a loop that allows the user to go through 
all three games before ending the program. '''