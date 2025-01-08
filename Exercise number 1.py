def calculadora(x: float,y:float):
    print("A soma destes números é igual a:",x+y)
    print("A subtração entre esses números é igual a:",x-y)
    print("O produto destes números é igual a:",x*y)
    print("A divisão entre estes números é igual a:",x/y)
    print("A divisão inteira entre estes números é igual a:",x//y)


x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

calculadora(x,y)