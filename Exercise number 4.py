def calculator(operation, x, y):
    match operation:
        case "+":
            print("A soma entre eles é:",x+y)
        case "-":
            print("A subtração entre eles é:",x-y)
        case "*":
            print("A multiplicação entre eles é:",x*y)
        case "/":
            if(y != 0):
                print("A divisão entre eles é:",x/y)
            else:
                print("Erro: Não é possível fazer uma divisão por 0.")
        case _:
            print("Operação inválida.")

a = input("Digite o símbolo da operação que deseja realizar: +, -, * ou / ")
b = float(input("Digite o primeiro número:"))
c = float(input("Digite o segundo número:"))

calculator(a,b,c)