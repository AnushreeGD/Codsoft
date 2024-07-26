from functions import *

while True:
    print("choose any option")
    print("1 Addition")
    print("2 Subtraction")
    print("3 Multiplication")
    print("4 division")
    print("press Q key to exit")

    choice = input("enter your choice : ")

    if choice == 'q' or choice == 'Q':
        break

    num1 = float(input("enter the number 1 : "))
    num2 = float(input("enter the number 2 : "))

    if choice == '1':
        addition(num1,num2)
    elif choice == '2':
        subtraction(num1,num2)
    elif choice == '3':
        multiplication(num1,num2)
    elif choice == '4':
        division(num1,num2)
    else:
        print("Invalid choice") 
