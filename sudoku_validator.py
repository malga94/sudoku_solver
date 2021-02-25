def read_board():

    with open("./board.txt", 'r') as f:
        data = f.read()

    board = []

    data = data.splitlines()
    for line in data:
        temp = line.split(',')
        board.append(temp)
    return board

def nest_array(board):

    x, temp = [], []
    cont = 0
    for elem in board:
        temp.append(elem)
        if cont%9 == 8:
            x.append(temp)
            temp = []
        cont += 1

    return x

def transpose_board(board):
    board_T = []
    for i in range(len(board[0])):
        l = []
        for elem in board:
            l.append(elem[i])

        board_T.append(l)

    return board_T

def get_3by3_subsectors(board):

    l = []
    for n in range(3):
        #Get three consecutive lines of the board
        a = board[3*n:3*(n+1)]
        for k in range(3):
            #Get elements from 0:3, from 3:6 and from 6:9 of these lines
            subsector = [[a[i][j] for j in range(3*k,3*(k+1))] for i in range(3)]
            flat_s = [x for sec in subsector for x in sec]
            l.append(flat_s)

    return l

def check_board(board):

    for row in board:
        row = [x for x in row if x!="."]
        for elem in row:
            if row.count(elem) > 1:
                return False

    return True

def is_valid(board):

    board = nest_array(board)
    #check lines
    req_1 = check_board(board)

    #check columns
    board = transpose_board(board)
    req_2 = check_board(board)

    #check subsectors
    board = get_3by3_subsectors(board)
    req_3 = check_board(board)

    if req_1 and req_2 and req_3:
        return True

    else:
        return False
