def even_or_dot(number):
    type_of_number = "even" if number % 2 == 0 else "dot"
    if type_of_number == "even": 
        print(f"You entered the number {number}. It's an {type_of_number} number.") 
    else: 
        print(f"You entered the number {number}. It's a {type_of_number} number.") 

number = int(input("Enter an integer: "))
even_or_dot(number)
