from random import randint

def make_move_steepest_hill(board):
    moves = {}
    for col in range(len(board)):
        best_move = board[col]

        for row in range(len(board)):
            if board[col] == row:
                # We don't need to evaluate the current
                # position, we already know the h-value
                continue

            board_copy = list(board)
            # Move the queen to the new row
            board_copy[col] = row
            moves[(col, row)] = get_h_cost(board_copy)

    best_moves = []
    h_to_beat = get_h_cost(board)
    for k, v in moves.items():
        if v < h_to_beat:
            h_to_beat = v

    for k, v in moves.items():
        if v == h_to_beat:
            best_moves.append(k)

    # Pick a random best move
    if len(best_moves) > 0:
        pick = randint(0, len(best_moves) - 1)
        col = best_moves[pick][0]
        row = best_moves[pick][1]
        board[col] = row

    return board


def get_h_cost(board):
    h = 0
    for i in range(len(board)):
        # Check every column we haven't already checked
        for j in range(i + 1, len(board)):
            # Queens are in the same row
            if board[i] == board[j]:
                h += 1
            # Get the difference between the current column
            # and the check column
            offset = j - i
            # To be a diagonal, the check column value has to be
            # equal to the current column value +/- the offset
            if board[i] == board[j] - offset or board[i] == board[j] + offset:
                h += 1

    return h
tab=[66, 69, 91, 49, 69, 27, 90, 41, 46, 57, 59, 68, 52, 29, 76, 25, 73, 6, 61, 9, 57, 83, 22, 72, 61, 52, 58, 53, 42, 33, 11, 72, 48, 26, 73, 73, 97, 89, 96, 46, 75, 27, 64, 58, 64, 87, 87, 51, 85, 86, 19, 56, 42, 24, 8, 70, 4, 98, 24, 8, 65, 35, 100, 60, 44, 54, 55, 35, 43, 63, 91, 69, 32, 79, 35, 62, 69, 86, 63, 15, 38, 80, 77, 62, 32, 60, 40, 25, 95, 56, 12, 70, 53, 11, 14, 76, 44, 42, 68, 97]
while 1:
    print(make_move_steepest_hill(tab))