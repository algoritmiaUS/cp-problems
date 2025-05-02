import string

letter = input()

if letter in ('A', 'E', 'I', 'O', 'U'):
    print("Jebb")
elif letter == 'Y':
    print("Kannski")
elif letter.isalpha():
    print("Neibb")
else:
    print("Kannski")