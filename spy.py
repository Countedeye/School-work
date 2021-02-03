print("What is your OP code?")
opCode = int(input())
if (opCode ==1):
    print("What is your spy name?")
    spyName = input()
    if len(spyName) == 5:
        print("Your mission has been aborted")
    elif len(spyName) == 10:
        print("You're in danger! Please evacuate to your safety location.")
    else:
        print("this program is self-destructing.")
elif (opCode ==2):
    print("input two different integers now.")
    int1 = input()
    int2 = input()
    sum = int(int1) + int(int2)
    spyName = "Jerry"
    print(spyName + str(sum))
elif (opCode ==3):
    print("What year were you born?")
    year = int(input())
    currentYear = 2021
    age = currentYear - year
    if age > 65:
        print("You are retired.")
    elif age <=65 and age >=41:
        print("You should apply for a promotion.")
    elif age  <=40 and age >=31:
        print("Keep working hard!")
    elif age <30:
        print("Go get some real world experience before becoming a spy!")
else:
    print("invaild OP code.")

