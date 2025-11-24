choice = input("Welcome to Quick Math Calculater! Do you want to do addition or subtraction?")

if choice == "addition":
    print("You chose addition.")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 + num2
    print("The answer is:" + str(sum))

elif choice == "subtraction":
    print("You chose subtraction")
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    sum = num1 - num2
    print("The answer is:" + str(sum))

else:
    print("Please choose either addition or subtraction.")