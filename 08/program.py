from itertools import chain

lines = list(map(lambda x: tuple(map(lambda y: y.split(), x.split('|'))), open('input.txt').read().splitlines()))
answer1 = len(list(filter(lambda x: len(x) in [2, 3, 4, 7], chain.from_iterable([x[1] for x in lines]))))

print(answer1)
