from collections import Counter

fish = list(map(int, open('input.txt').read().split(',')))

def age(f):
    return list(map(lambda x: x - 1, f))

def count_ready(f):
    return len(list(filter(lambda x: x < 0, f)))

def spawn(f):
    return list(map(lambda x: x if x >= 0 else 6, f)) + [8] * count_ready(f)

def day(f):
    return spawn(age(f))

f = fish
for i in range(80):
    f = day(f)

answer1 = len(f)

print(answer1)

# part 2

fc = dict(Counter(fish).items())

def dayv2(f):
    new = dict()
    for i in range(0, 9):
        new[i - 1] = f.get(i, 0)
    new[6] = new.get(6, 0) + new.get(-1, 0)
    new[8] = new.get(-1, 0)
    del new[-1]
    return new

for i in range(0, 256):
    fc = dayv2(fc)

answer2 = sum(fc.values())

print(answer2)
