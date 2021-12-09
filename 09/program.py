from math import prod

input = list(map(lambda line: list(map(int, list(line))), open('input.txt').read().splitlines()))
ymax = len(input) - 1
xmax = len(input[0]) - 1

lps = set()
for y, line in enumerate(input):
    for x, el in enumerate(line):
        me = input[y][x]
        nn = input[y - 1][x] if y > 0 else 10
        ne = input[y][x + 1] if x < xmax else 10
        ns = input[y + 1][x] if y < ymax else 10
        nw = input[y][x - 1] if x > 0 else 10
        ismin = me < nn and me < ne and me < ns and me < nw
        if ismin:
            lps.add((x, y))

answer1 = sum([input[y][x] for (x, y) in lps]) + len(lps)

print(answer1)

# part 2

def basin_members(lp, found=set()):
    if lp in found:
        return set()
    res = set()
    res.add(lp)
    x, y = lp
    if y > 0:
        nn = (x, y - 1)
        if input[nn[1]][nn[0]] < 9:
            res |= basin_members(nn, found | res)
    if x < xmax:
        ne = (x + 1, y)
        if input[ne[1]][ne[0]] < 9:
            res |= basin_members(ne, found | res)
    if y < ymax:
        ns = (x, y + 1)
        if input[ns[1]][ns[0]] < 9:
            res |= basin_members(ns, found | res)
    if x > 0:
        nw = (x - 1, y)
        if input[nw[1]][nw[0]] < 9:
            res |= basin_members(nw, found | res)
    return res

answer2 = prod(sorted([len(basin_members(lp)) for lp in lps], reverse=True)[0:3])

print(answer2)
