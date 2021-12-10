lines = open('input.txt').read().splitlines()

pairs = {')': '(', ']': '[', '}': '{', '>': '<'}
openers = pairs.values()
closers = pairs.keys()

points = {')': 3, ']': 57, '}': 1197, '>': 25137}

def check_corrupt(line):
    stack = []
    for ch in line:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            if stack.pop() != pairs[ch]:
                return points[ch]
    return 0

answer1 = sum([check_corrupt(line) for line in lines])

print(answer1)

# part 2

incomp = [line for line in lines if not check_corrupt(line)]

points2 = {'(': 1, '[': 2, '{': 3, '<': 4}

def complete(line):
    stack = []
    for ch in line:
        if ch in openers:
            stack.append(ch)
        elif ch in closers:
            stack.pop()
    score = 0
    for x in reversed(stack):
        score = score * 5 + points2[x]
    return score

scores = sorted([complete(line) for line in incomp])
answer2 = scores[(len(scores) + 1) // 2 - 1]

print(answer2)
