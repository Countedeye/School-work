print("Enter a number:")
# first user number.
x_str = input()
x = float(x_str)
print("Enter a second number:")
# second user number.
y_str = input()
y = float(y_str)
# Asks user for operations.
print("Which mathmatical operation would you like to perform on your two numbers?")
print("Options:")
# list of options
print(" Addition.")
print(" Subtraction.")
print(" Multiplication.")
print(" Division.")
print(" Integer Division.")
print(" Modulus.")
print(" Exponentiation.")
operation = input()
operation = operation.lower()
operation = operation.strip()
# conditions and outputs.
if operation == "addition": 
    print("The result is", x + y)
elif operation == "subtraction":    
    print("The result is", x - y)
elif operation == "multiplication":
    print("The result is", x * y)
elif operation == "division":
    print("The result is", x // y) 
elif operation == "integer division":
    print("The result is", x / y)
elif operation == "modulus":
    print("The result is", x % y)
elif operation == "exponentiation":
    print("The result is", x ** y)
else:
    print("Unrecognized option \"" + operation +"\" given.")