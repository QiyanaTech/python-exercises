def calculator(operation, x, y):
    match operation:
        case "+":
            print("The sum between then is: ",x+y)
        case "-":
            print("The subtraction between then is :",x-y)
        case "*":
            print("The multiplication between then is:",x*y)
        case "/":
            if(y != 0):
                print("The division between then is:",x/y)
            else:
                print("Error: Can't do a division by 0.")
        case _:
            print("Invalid operation.")

a = input("Enter the symbol of operation you want to perform: +, -, * or / ")
b = float(input("Enter the first number: "))
c = float(input("Enter the second number: "))

calculator(a,b,c)