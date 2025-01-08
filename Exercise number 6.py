def find_out_the_number(number:int):
    if (number >= 14):
        print("You're far from the number.")
    elif (number >= 11 and number <= 13):
        print("You're close to the number.")
    elif (number == 10):
        print("You found the number!")
    elif (number >= 7 and number <= 9):
        print("You're close to the number.")
    else:
        print("You're far from the number.")

find_out_the_number(int(input("Try to find a number between 0 and 15: ")))