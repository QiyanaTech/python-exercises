def hours_calculator(minutes:int):
    hours = minutes // 60
    minutes_left = minutes % 60
    if hours == 1:
        print(f"{hours} hour and {minutes_left} minutes.")
    else:
        print(f"{hours} hours and {minutes_left} minutes.")

def minutes_calculator(hours:int,minutes:int):
    total_minutes = minutes + hours * 60
    print(f"{total_minutes} total minutes.")

a = int(input("Enter the number of minutes to calculate the number of hours and minutes: "))
hours_calculator(a)

b = int(input("Now, enter the number of hours and minutes to calculate the total minutes. Hours:"))
c = int(input("Minutes:"))
minutes_calculator(b,c)