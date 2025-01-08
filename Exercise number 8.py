def is_legal_age(age):
    print("You are of legal age.") if age >= 18 else print("You aren't of legal age.")

is_legal_age(int(input("Enter your age: ")))