input = list(map(lambda l: list(map(int, l)), open('input.txt').read().splitlines()))

grid = {}
for y, line in enumerate(input):
    for x, num in enumerate(line):
        grid[(x, y)] = num

maxx = max(map(lambda el: el[0], grid.keys()))
maxy = max(map(lambda el: el[1], grid.keys()))

def path(grid):
    maxx = max(map(lambda el: el[0], grid.keys()))
    maxy = max(map(lambda el: el[1], grid.keys()))

    dist = {}
    for p in grid.keys():
        dist[p] = None

    unvisited = set(grid.keys())
    curx, cury = (0, 0)
    dist[(0, 0)] = 0

    while True:
        for dirx, diry in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nb = (curx + dirx, cury + diry)
            if nb not in unvisited:
                continue
            newdist = dist[(curx, cury)] + grid[nb]
            if dist[nb] is None or newdist < dist[nb]:
                dist[nb] = newdist
        unvisited.remove((curx, cury))
        if (maxx, maxy) not in unvisited:
            break
        smallest = None
        for uv in unvisited:
            if smallest is None or (dist[uv] is not None and dist[uv] < smallest):
                smallest = dist[uv]
                next = uv
        curx, cury = next

    return dist[(maxx, maxy)]

answer1 = path(grid)

print(answer1)

# part 2

maxx = max(map(lambda el: el[0], grid.keys()))
maxy = max(map(lambda el: el[1], grid.keys()))
grid2 = {}

for xx in range(0, 5):
    for yy in range(0, 5):
        for p, v in grid.items():
            newv = (grid[p] + (xx + yy))
            if newv > 9:
                newv -= 9
            grid2[(p[0] + (maxx + 1) * xx, p[1] + (maxy + 1) * yy)] = newv

answer2 = path(grid2)

print(answer2)
