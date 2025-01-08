def find_out_the_number(number:int):
    if (number >= 14):
        print("Você está distante do número.")
    elif (number >= 11 and number <= 13):
        print("Você está próximo do número.")
    elif (number == 10):
        print("Você descobriu o número!")
    elif (number >= 7 and number <= 9):
        print("Você está próximo do número.")
    else:
        print("Você está distante do número.")

find_out_the_number(int(input("Tente descobrir um número entre 0 e 15:")))