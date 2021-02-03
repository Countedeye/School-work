import random


rand1 =random.randint(0,10)
rand2 =random.randint(0,10)
print(str(rand1) + "+" + str(rand2)+ "=")
userinput = input()
answer = rand1 + rand2
if (int(userinput) == int(answer)):
    print("Good job!")
else:
    print("Sorry! The correct number is:")
    print(answer) 
rand1 =random.randint(0,10)
rand2 =random.randint(0,10)
print(str(rand1) + "*" + str(rand2) + "=")
userinput = input()
answer = rand1 * rand2
if (int(userinput) == int(answer)):
    print("Good job!")
else:
    print("Sorry! The correct number is:")
    print(answer)
rand1 =random.randint(0,10)
rand2 =random.randint(1,10) 
print(str(rand1) + "/" + str(rand2) + "=")
userinput =input()
answer = rand1 /rand2
if (int(userinput) == int(answer)):
    print("Good job!")
else:
    print("Sorry! The correct number is:")
    print(float(answer))
