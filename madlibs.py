import sys

def get_word():

    return input('Enter a word: ')

def parse_args(args):

    return args[1:]

args = parse_args(sys.argv)

for index in range(len(args)):

    if args[index] == '_':

        args[index] = get_word()

result = ' '.join(args)

print(result)
print(args)
print(sys.argv)
