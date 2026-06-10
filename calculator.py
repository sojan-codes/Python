def addition() :
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the Second number: "))
    return value1 + value2

def substraction() :
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the Second number: "))
    return value1 - value2

def multiplication() :
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the Second number: "))
    return value1 / value2

def division() :
    value1 = float(input("Enter the first number: "))
    value2 = float(input("Enter the Second number: "))
    return value1 / value2


def calculator():
    print("Enter 1 for Addition:")
    print("Enter 2 for Substraction:")
    print("Enter 3 for Multiplication:")
    print("Enter 3 for Division:")


while True:
    print("----Calculator----")
    calculator()
    choice = input("\nChoose an operation(1/2/3/4) or 'q' to quit: ")
    if choice == 'q':
        print("Exiting the calculator. Goodbye!")
        break

    if choice == '1':
        print("the result of addition is: ", addition())
    elif choice =='2':
        print("The result of Substraction is :", substraction())
    elif choice =='3':
        print("The result of Multiplication is :", multiplication())
    elif choice =='4':
        print("The result of Division is :", division())

