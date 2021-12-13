import re

input = open('input.txt').read().splitlines()
points = set(map(lambda x: tuple(map(int, x.split(','))), input[:input.index('')]))
instrs = input[input.index('') + 1:]

def fold(points, instr):
    m = re.fullmatch(r'fold along (\w)=(\d+)', instr)
    axis = m.group(1)
    line = int(m.group(2))
    newpoints = set()
    if axis == 'x':
        for p in points:
            if p[0] < line:
                newpoints.add(p)
            else:
                newpoints.add((line - (p[0] - line), p[1]))
    elif axis == 'y':
        for p in points:
            if p[1] < line:
                newpoints.add(p)
            else:
                newpoints.add((p[0], line - (p[1] - line)))
    return newpoints

answer1 = len(fold(points, instrs[0]))

print(answer1)

# part 2

for instr in instrs:
    points = fold(points, instr)

out = ''
for y in range(0, max(map(lambda p: p[1], points)) + 1):
    for x in range(0, max(map(lambda p: p[0], points)) + 1):
        out += '#' if (x, y) in points else '.'
    out += '\n'

print(out)
