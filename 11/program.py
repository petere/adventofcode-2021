input = list(map(lambda l: list(map(int, l)), open('input.txt').read().splitlines()))

grid = {}
for y, line in enumerate(input):
    for x, num in enumerate(line):
        grid[(x, y)] = num

def step(grid):
    flashes = 0
    for k, v in grid.items():
        grid[k] = v + 1
    for k, v in grid.items():
        flashes += maybe_flash(k, grid)
    for k, v in grid.items():
        if v is None:
            grid[k] = 0
    return grid, flashes

def maybe_flash(pos, grid):
    if grid[pos] is None or grid[pos] <= 9:
        return 0
    flashes = 1
    grid[pos] = None
    x, y = pos
    for adj in [(x - 1, y - 1), (x, y - 1), (x + 1, y - 1),
                (x - 1, y), (x + 1, y),
                (x - 1, y + 1), (x, y + 1), (x + 1, y + 1)]:
        if grid.get(adj) is not None:
            grid[adj] = grid[adj] + 1
            flashes += maybe_flash(adj, grid)
    return flashes

flashes = 0
for _ in range(0, 100):
    grid, nf = step(grid)
    flashes += nf

print(flashes)

# part 2

i = 100
while True:
    grid, nf = step(grid)
    i += 1
    if nf == 100:
        break

print(i)
