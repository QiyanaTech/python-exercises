def hours_calculator(minutes:int):
    hours = minutes // 60
    minutes_left = minutes % 60
    print(f"{hours}h{minutes_left}.")

def minutes_calculator(hours:int,minutes:int):
    total_minutes = minutes + hours * 60
    print(f"{total_minutes} minutos totais.")

a = int(input("Digite o número de minutos para calcular o número de horas e minutos:"))
hours_calculator(a)

b = int(input("Agora digite o número de horas e minutos para calcular o número de minutos totais. Horas:"))
c = int(input("Minutos:"))
minutes_calculator(b,c)