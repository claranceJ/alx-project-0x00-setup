#Palindrome
#Create a function is_palindrome(word) that returns True if a given word is a palindrome
# (reads the same backward) and False otherwise.
def is_palindrome(word):
    return word == word[::-1] #slice method that reverses a word

word = input('Enter a word: ')
answer =is_palindrome(word)

if answer:
    print('True')
else:
    print('False')