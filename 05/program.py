from collections import Counter
import re

textlines = open('input.txt').read().splitlines()

def parse_line(ln):
    if m := re.fullmatch(r'(\d+),(\d+) -\> (\d+),(\d+)', ln):
        x1 = int(m.group(1))
        y1 = int(m.group(2))
        x2 = int(m.group(3))
        y2 = int(m.group(4))
        return ((x1, y1), (x2, y2))

linesegs = list(map(parse_line, textlines))

ver = list(filter(lambda ls: ls[0][0] == ls[1][0], linesegs))
hor = list(filter(lambda ls: ls[0][1] == ls[1][1], linesegs))

grid = Counter()

for ls in ver:
    p1, p2 = ls
    step = 1 if p1[1] < p2[1] else -1
    pts = [(p1[0], y) for y in range(p1[1], p2[1] + step, step)]
    grid.update(pts)

for ls in hor:
    p1, p2 = ls
    step = 1 if p1[0] < p2[0] else -1
    pts = [(x, p1[1]) for x in range(p1[0], p2[0] + step, step)]
    grid.update(pts)

answer1 = len(list(filter(lambda x: x[1] >= 2, grid.items())))

print(answer1)

# part 2

dia = list(filter(lambda ls: ls[0][1] != ls[1][1] and ls[0][0] != ls[1][0], linesegs))

for ls in dia:
    p1, p2 = ls
    stepx = 1 if p1[0] < p2[0] else -1
    stepy = 1 if p1[1] < p2[1] else -1
    pts = zip([x for x in range(p1[0], p2[0] + stepx, stepx)],
              [y for y in range(p1[1], p2[1] + stepy, stepy)])
    grid.update(pts)

answer2 = len(list(filter(lambda x: x[1] >= 2, grid.items())))

print(answer2)
