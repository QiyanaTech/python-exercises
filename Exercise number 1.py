def calculator(x: float,y:float):
    print("The sum of these numbers is: ",x+y)
    print("The substration of these numbers is: ",x-y)
    print("The product of these numbers is: ",x*y)
    print("The division between these numbers is: ",x/y)
    print("The integer division between these number is: ",x//y)

x = int(input("Enter the first number: "))
y = int(input("Enter the second number:  "))

calculator(x,y)