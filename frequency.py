import sys

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'

args = sys.argv[1:]

for arg in args:

    print(arg)

text = ''.join(args)

print(text)

lowercase_letter = text[0].lower()

print(lowercase_letter)

lowercase_text = text.lower()

print(lowercase_text)

frequencies = {}

for letter in ALPHABET:

    frequencies[letter] = 0

for letter in lowercase_text:

    frequencies[letter] += 1

print(frequencies)

for letter in ALPHABET:

    count = frequencies[letter]

    print(letter, end=' ')

    for c in range(count):

        print('|', end='')

    print()
