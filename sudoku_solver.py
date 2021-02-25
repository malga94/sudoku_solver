from sudoku_validator import is_valid, nest_array, read_board

def flatten_array(l):

    flat_l = []
    for line in l:
        for elem in line:
            flat_l.append(elem)

    return(flat_l)

def solve_board(board, pos, empty_pos):

    if pos == len(empty_pos):
        for line in nest_array(board):
            print(str(line) + '\n')
        exit()

        return board, True
    x = 1

    if board[empty_pos[pos]] != '.':
        x = int(board[empty_pos[pos]]) + 1

    for i in range(x, 10):
        board[empty_pos[pos]] = str(i)
        if is_valid(board):
            b, y = solve_board(board, pos+1, empty_pos)
            if y:
                return b, y
        else:
            continue

    board[empty_pos[pos]] = '.'
    return board, False

def main():

    board = read_board()
    flat_board = flatten_array(board)

    for cont, elem in enumerate(flat_board):
        if elem == 0:
            flat_board[cont] = '.'
        else:
            flat_board[cont] = str(flat_board[cont])

    if not is_valid(flat_board):
        s = "This is not a valid sudoku board!"
        return [], s

    empty_pos = []
    for square, val in enumerate(flat_board):
        if val == '.':
            empty_pos.append(square)

    board, x = solve_board(flat_board, 0, empty_pos)

    if x:
        s = "Board solved!"
        return board, s
    else:
        s = "This board is not solvable"
        return [], s

if __name__ == '__main__':
    main()
