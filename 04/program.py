from itertools import chain

lines = open('input.txt').read().splitlines()

cards = lines[0].split(',')

boardrows = list(map(lambda x: x.split(), lines[2:]))
boards = [list(chain(*boardrows[i:i + 5])) for i in range(0, len(boardrows), 6)]
boardstates = list(map(lambda board: list(map(lambda x: (x, False), board)), boards))

def row_wins(row):
    return all(map(lambda x: x[1], row))

def check_winner(board):
    rows = [board[i:i + 5] for i in range(0, len(board), 5)]
    cols = list(map(list, zip(*rows)))
    return len(list(filter(row_wins, rows + cols))) >= 1

def apply_card(card, boardstate):
    return list(map(lambda b: list(map(lambda x: (x[0], x[1] or x[0] == card), b)), boardstate))

boardswon = len(boardstates) * [False]
scores = []
for card in cards:
    won = False
    boardstates = apply_card(card, boardstates)
    for i, b in enumerate(boardstates):
        if boardswon[i]:
            continue
        if check_winner(b):
            scores.append(int(card) * sum([int(x[0]) for x in b if not x[1]]))
            boardswon[i] = True

print(scores[0])

# part 2

print(scores[-1])
