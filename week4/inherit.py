import itertools

String = input('Type a word: ')
com = itertools.permutations(String)

for val in com:
    print(*val)