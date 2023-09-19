#This is a Simple Calculator Program.
print("Welcome,This is a simple Calculator")
print("Select an operation to perform:")
print("1.Addition")
print("2.Subtraction")
print("3.Multiplication")
print("4.Division")
print("5.Power of a Number")
print("6.Square of a Number")
a = int(input()) #takes the input selection from the user for the operation.

if a == 1:
    print("This is addition")
    x = int(input("Enter First Number:\n")) #takes first integer number
    y = int(input("Enter Second Number:\n")) #takes second integer number
    print("The Sum of these 2 numbers is :", x+y) #prints the sum of these 2 numbers

elif a == 2:
    print("This is subtraction")
    x = int(input("Enter First Number:\n")) #takes first integer number
    y = int(input("Enter Second Number:\n")) #takes second integer number
    print("The Difference of these 2 numbers is:",x-y) #prints the difference of these 2 numbers

elif a == 3:
    print("This is Multiplication")
    x = int(input("Enter First Number:\n")) #takes first integer number
    y = int(input("Enter Second Number:\n")) #takes second integer number
    print("The Multiplication of these 2 numbers is:",x*y) #prints the multiplication of these 2 numbers

elif a == 4:
    print("This is Division")
    x = int(input("Enter First Number(Numerator):\n")) #takes first integer number
    y = int(input("Enter Second Number(Denominator):\n")) #takes second integer number
    print("The Division of these 2 numbers is:",x/y) #prints the division of these 2 numbers.
elif a == 5:
    print("Power of a Number")
    x = int(input("Enter the number:\n"))
    y = int(input("Enter the power you want to raise the number to:"))
    print("The result of",x,"raise to power",y,"is",x**y)
elif a == 6:
    print("Square of a number")
    x = int(input("Enter the number:\n"))
    print("Square of this number is:",x*x)

else:
    print("Invalid Input,Please Re-Run and input valid entery")
