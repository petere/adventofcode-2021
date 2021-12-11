from itertools import chain

lines = list(map(lambda x: tuple(map(lambda y: y.split(), x.split('|'))), open('input.txt').read().splitlines()))
answer1 = len(list(filter(lambda x: len(x) in [2, 3, 4, 7], chain.from_iterable([x[1] for x in lines]))))

print(answer1)

# part 2

def decode(codes):
    values = {}
    rvalues = {}
    for code in codes:
        n = len(code)
        if n == 2:
            values[code] = 1
            rvalues[1] = code
        elif n == 3:
            values[code] = 7
            rvalues[7] = code
        elif n == 4:
            values[code] = 4
            rvalues[4] = code
        elif n == 7:
            values[code] = 8
    for code in codes:
        n = len(code)
        if n == 6:
            if set(code) > set(rvalues[7]) | set(rvalues[4]):
                values[code] = 9
            elif set(code) > set(rvalues[1]):
                values[code] = 0
            else:
                values[code] = 6
                rvalues[6] = code
    for code in codes:
        n = len(code)
        if n == 5:
            if set(code) > set(rvalues[1]):
                values[code] = 3
            elif set(code) < set(rvalues[6]):
                values[code] = 5
            else:
                values[code] = 2
    return values

answer2 = 0
for line in lines:
    obs, out = tuple(map(lambda y: list(map(lambda x: ''.join(sorted(x)), y)), line))
    c = decode(obs)
    v = 0
    for i, d in enumerate(reversed(out)):
        v += 10**i * c[d]
    answer2 += v

print(answer2)
