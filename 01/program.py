from itertools import starmap
from operator import lt, truth

n = list(map(int, open('input.txt').read().splitlines()))
n1 = n[1:]
z = zip(n, n1)
answer1 = len(list(filter(truth, starmap(lt, z))))

print(answer1)

# part 2

n2 = n[2:]
w = zip(n, n1, n2)
ws = list(map(sum, w))
ws1 = ws[1:]
z2 = zip(ws, ws1)
answer2 = len(list(filter(truth, starmap(lt, z2))))

print(answer2)
