from collections import Counter

input = open('input.txt').read().splitlines()
template = input[0]
rules = dict(map(lambda x: tuple(x.split(' -> ')), input[2:]))

def step(inp):
    outp = ''
    for i, c in enumerate(inp):
        outp += c
        if n := rules.get(inp[i: i + 2]):
            outp += n
    return outp

pol = template
for i in range(0, 10):
    pol = step(pol)

cnt = Counter(pol)
answer1 = max(cnt.values()) - min(cnt.values())

print(answer1)

# part 2

pairs = Counter()
for i, c in enumerate(template[:-1]):
    pairs[template[i: i + 2]] += 1

for i in range(0, 40):
    oldpairs = pairs.copy()
    for p in oldpairs.keys():
        if n := rules.get(p):
            pairs[p] -= oldpairs[p]
            pairs[p[0] + n] += oldpairs[p]
            pairs[n + p[1]] += oldpairs[p]

cnt2 = Counter()
for p, v in pairs.items():
    cnt2[p[1]] += v

answer2 = max(cnt2.values()) - min(cnt2.values())

print(answer2)
