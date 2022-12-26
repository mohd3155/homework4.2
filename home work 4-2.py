
num1 = input("please enter the first number")

if num1.isdigit():
    opr = input("please choose an operation")
    if opr == '1' or opr == '+':
        num2 = input("Please enter the second number")
        print(int(num1) + int(num2))

    elif opr == '2' or opr == '-':
        num2 = input("Please enter the second number")

        print(int(num1) - int(num2))

    elif opr == '3' or opr == '*':
        num2 = input("Please enter the second number")
        print(int(num1) * int(num2))

    elif opr == '4' or opr == '/':
        num2 = input("Please enter the second number")
        print(int(num1) / int(num2))

    elif opr == '5' or opr == '^':
        num2 = input("Please enter the second number")
        print(int(num1) ^ int(num2))

    elif opr == '6' or opr == '%':
        num2 = input("Please enter the second number")
        print(int(num1) % int(num2))

else:
    print("Error")

