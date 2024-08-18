# Get the first number from the user
n1 = int(input("Enter first number: "))

# Get the expression from the user
exp = input("Enter the expression: ")

# Get the second number from the user
n2 = int(input("Enter second number: "))

# Perform the operation based on the expression
if exp == "+":
    print(n1 + n2)
elif exp == "-":
    print(n1 - n2)
elif exp == "*":
    print(n1 * n2)
elif exp == "/":
    if n2 != 0:  # Check for division by zero
        print(n1 / n2)
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Please enter a valid expression.")

# Ask the user if they want to play again
play_again = input("If you want to continue, press 'y', or press any other key to exit: ")
if play_again.lower() != 'y':
    print("Exit.")