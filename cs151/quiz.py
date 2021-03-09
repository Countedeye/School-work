#grades.py - in this program, you will ask the user for a numeric grade. 
# Then, you will convert the grade to a letter grade, 
# and print out "You got a(n) " and the letter grade.  
# If they got an A or a B, print out "Good job!".  
# If they have a D or an F, print out "Study some more!".   
# Use the following scale:
#A: 90-100
#B: 80-89
#C: 70-79,
#D: 60-69
#F: below 60
print("What was your numeric grade?")
grade = int(input())
if grade <=100 and grade >=90:  #letter grade A
    print("you received an A")
    print("Good job!")
elif grade <=89 and grade >=80: #letter grade B
    print("you received a B")
    print("Good job!")
elif grade <=79 and grade >=70: #letter grade C
    print("you received a C")
elif grade <=69 and grade >=60: #letter grade D
    print("you received a D")
    print("Study some more!")
elif grade <=59 and grade >=0:  #letter grade F
    print("you received a F")
    print("Study some more!")
else:
    print("invalid entry.")

