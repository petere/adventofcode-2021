from functools import reduce

pos = list(map(int, open('input.txt').read().split(',')))

_, answer1 = reduce(lambda x, y: x if x[1] < y[1] else y,
                    [(meet, sum([abs(x - meet) for x in pos])) for meet in range(min(pos), max(pos) + 1)])

print(answer1)

_, answer2 = reduce(lambda x, y: x if x[1] < y[1] else y,
                    [(meet, sum([(abs(x - meet)**2 + abs(x - meet)) // 2 for x in pos])) for meet in range(min(pos), max(pos) + 1)])

print(answer2)
