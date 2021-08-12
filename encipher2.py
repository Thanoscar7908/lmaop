import sys

ALPHABET = 'abcefghijklmnopqristuvwxyz'
KEY = 'QWERTYUIOPASDFGHJKLZXCVBNM'
args = sys.argv[1:]

for arg in args:

    print(arg)

text = ' '.join(args)

print(text)

lowercase_letter = text[0].lower()

print(lowercase_letter)

#lowercase_text = [letter.lower() for letter in text]
lowercase_text = text.lower()

print(lowercase_text)

' '.join(lowercase_text)

frequencies = {}

for letter in ALPHABET:

        frequencies[letter] = 0

for letter in text:

        if letter not in frequencies:

                frequencies[letter] = 1

        else:
             
                frequencies[letter] += 1

print(frequencies)

for letter in ALPHABET:
    
    count = frequencies[letter]

    print(letter, end=' ')

    for c in range(count):

            print('l', end='')

    print()
