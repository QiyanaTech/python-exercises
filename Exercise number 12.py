def long_or_short(word):
    print("This is a short word.") if len(word) < 5 else print("This is a long word.")

long_or_short(input("Enter a word: "))