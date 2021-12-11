def try_board(board_raw):

    board_lines = board_raw.split("\n")
    board = []
    for line in board_lines:
        board.append(list(map(int, line.split())))

    lowest_index = 100
    # for line check highest index
    for row in board:
        highest_index = 0
        for num in row:
            num_idx = order.index(num)
            if num_idx > highest_index:
                highest_index = num_idx

        if highest_index < lowest_index:
            lowest_index = highest_index


    print(board)
    # for column check highest index
    for col in range(len(board[0])):
        highest_index = 0
        for line in board:
            num_idx = order.index(line[col])
            if num_idx > highest_index:
                highest_index = num_idx

        if highest_index < lowest_index:
            lowest_index = highest_index

    # return lowest index
    return lowest_index


if __name__ == "__main__":
    with open("input.txt") as fp:
        inp = fp.read()

    order, *boards = inp.split("\n\n")

    order = list(map(int, order.split(',')))


    current_idx = len(order)
    current_board = None
    
    for board in boards:
        idx = try_board(board)
        if idx < current_idx:
            current_idx = idx
            current_board = board

    final_num = order[current_idx]

    board_mod = set(map(int, current_board.replace('\n', ' ').split()))
    board_mod -= set(order[:current_idx+1])
        
    print(current_idx, final_num)
    print(sum(board_mod)*final_num)
    
