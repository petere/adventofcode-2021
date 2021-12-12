from collections import Counter

inlines = open('input.txt').read().splitlines()
edges = set()
for line in inlines:
    p = line.split('-')
    edges.add((p[0], p[1]))
    edges.add((p[1], p[0]))

def paths_from(inpath):
    ret = []
    for e in edges:
        if e[0] != inpath[-1]:
            continue
        if e[1].lower() == e[1]:
            if e[1] in inpath:
                continue
        newpath = inpath + [e[1]]
        if e[1] == 'end':
            ret.append(newpath)
        else:
            for paths in paths_from(newpath):
                ret.append(paths)
    return ret

answer1 = len(paths_from(['start']))

print(answer1)

# part 2

def may_visit(inpath, node):
    if node == 'start':
        return False
    elif node.lower() != node:
        return True
    elif node in inpath:
        c = Counter(inpath)
        for el, cnt in c.items():
            if el.lower() == el and cnt > 1:
                return False
        return True
    else:
        return True

def paths_from2(inpath):
    ret = []
    for e in edges:
        if e[0] != inpath[-1]:
            continue
        if not may_visit(inpath, e[1]):
            continue
        newpath = inpath + [e[1]]
        if e[1] == 'end':
            ret.append(newpath)
        else:
            for paths in paths_from2(newpath):
                ret.append(paths)
    return ret

answer2 = len(paths_from2(['start']))

print(answer2)
