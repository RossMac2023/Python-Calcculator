# Python calculator
# By Ross Mackay
user_choice = "temp"
num1 = 0
num2 = 0
total = 0

print("Welcome to the Python Calculator!")
print("Please select an operation:")
print("addition, subtraction, multiplication or division")
user_choice = input("")

# Addition
if user_choice == "addition":
  print("You have chosen addition")
  num1 = input("What is your first number?  ")
  num2 = input("What is your second number?  ")
  total = int(num1) + int(num2)
  print(total)

# Subtraction
elif user_choice == "subtraction":
  print("You have chosen subtraction")
  num1 = input("What is your first number?  ")
  num2 = input("What is your second number?  ")
  total = int(num1) - int(num2)
  print(total)

# Multiplication
elif user_choice == "multiplication":
  print("You have chosen multiplication")
  num1 = input("What is your first number?  ")
  num2 = input("What is your second number?  ")
  total = int(num1) * int(num2)
  print(total)

# Division
elif user_choice == "division":
  print("You have chosen division")
  num1 = input("What is your first number?  ")
  num2 = input("What is your second number?  ")
  total = int(num1) / int(num2)
  print(total)

input("The calculator has stopped. Press 'Run' to restart")
