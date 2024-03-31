word = input("Enter a word: ")
def palindrome(word):
    if word == word[::-1]:
        print("Your word is palindrome")
    else:
        print("Your word is not palindrome")
palindrome(word)