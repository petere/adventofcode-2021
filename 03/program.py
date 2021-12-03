from collections import Counter

diag = list(map(lambda x: list(map(int, x)), open('input.txt').read().splitlines()))
counts = list(map(Counter, zip(*diag)))

def bitseq_to_int(seq):
    return int(''.join(map(str, seq)), 2)

γ = bitseq_to_int(map(lambda x: x.most_common(1)[0][0], counts))
ε = bitseq_to_int(map(lambda x: 1 - x.most_common(1)[0][0], counts))
answer1 = γ * ε

print(answer1)

# part 2

def one_step(lst, bc, pos):
    counts = list(map(Counter, zip(*lst)))
    filter_bit = bc if counts[pos][1] - counts[pos][0] >= 0 else 1 - bc
    return list(filter(lambda x: x[pos] == filter_bit, lst))

def all_steps(lst, bc, pos=0):
    return all_steps(one_step(lst, bc, pos), bc, pos + 1) if len(lst) > 1 else lst

ov = bitseq_to_int(all_steps(diag, 1)[0])
cv = bitseq_to_int(all_steps(diag, 0)[0])
answer2 = ov * cv

print(answer2)
