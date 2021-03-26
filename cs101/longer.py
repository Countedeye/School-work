print("What is your name?")
username = input()
data1= input("Hello " + username + ", will you please write out a statement or sentence of your choice: " )
data2= input("Thank you " + username + ", now can you write another statement or sentence? ")
len1=len(data1)
print(username + ", I detected that string 1 was " + str(len1) + " characters long.")
len2=len(data2)
print(f"{username}, I detected that string 2 was {len2} characters long.")
if len(data1) > len(data2):
    print(f"{username}, I have determined that string 1 is longer.")
elif len(data2) > len(data1):
    print(f"{username}, I have determined that string 2 is longer.")
else:
    print("Oops we have and error somewhere.")