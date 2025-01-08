def imc_calculator(weight:float,height:float):
    imc = weight / height ** 2
    print(f"Your IMC is {imc}.")
    if(imc < 18.5):
        print("You are underweight.")
    elif (imc >= 18.5 and imc < 25):
        print("You have the appropriate weight.")
    elif (imc >= 25 and imc < 30):
        print("You are overweight.")
    elif (imc >= 30 and imc < 35):
        print("You have grade 1 obesity.")
    elif (imc >= 35 and imc < 40):
        print("You have grade 2 obesity.")
    else:
        print("You have grade 3 obesity.")

x = float(input("Please, enter your weight."))
y = float(input("Now, enter your height."))

imc_calculator(x,y)