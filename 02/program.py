from functools import reduce
import re


def parse(s):
    if m := re.fullmatch(r'forward (\d+)', s):
        return (int(m.group(1)), 0)
    elif m := re.fullmatch(r'down (\d+)', s):
        return (0, int(m.group(1)))
    elif m := re.fullmatch(r'up (\d+)', s):
        return (0, -int(m.group(1)))
    else:
        raise


steps = list(map(parse, open('input.txt').read().splitlines()))
dest = tuple([sum(i) for i in zip(*steps)])
answer1 = dest[0] * dest[1]

print(answer1)


# part 2


def move(pos, step):
    match step:
        case (f, 0):
            return (pos[0] + f, pos[1] + pos[2] * f, pos[2])
        case (0, a):
            return (pos[0], pos[1], pos[2] + a)


dest2 = reduce(move, steps, (0, 0, 0))
answer2 = dest2[0] * dest2[1]

print(answer2)
