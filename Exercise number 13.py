def is_palindrome(word):
    print("This word is a palindrome.") if word == word[::-1] else print("This word isn't a palindrome.")

word = input("Write a word without capital letters: ")

is_palindrome(word)
        