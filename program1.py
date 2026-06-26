num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("Addition =", num1 + num2)
print("Subtraction =", num1 - num2)
print("Multiplication =", num1 * num2)

if num2 != 0:
    print("Division =", num1 / num2)
else:
    print("Error: Division by zero is not allowed.")

# Output:
# Enter first number: 20
# Enter second number: 5
# Addition = 25.0
# Subtraction = 15.0
# Multiplication = 100.0
# Division = 4.0
