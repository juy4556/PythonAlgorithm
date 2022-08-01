import copy

N, M = map(int, input().split())
board = []
for _ in range(N):
    board.append(input())


def dfs(board, time):
    for i in range(4):
        new_board = copy.deepcopy(board)
        goal, new_board = move(i, new_board)
        if goal:
            return time
        dfs(new_board, time+1)


def move(dir, board):
    red, blue = [], []
    goal = False
    for i in range(1,N-1):
        for j in range(1,M-1):
            if board[i][j] == 'R':
                red = [i,j]
            elif board[i][j] == 'B':
                blue = [i,j]

    if dir == 0:  # up
        for i in range(red[0], 1, -1):
            if board[i-1][red[1]] == '#':
                break
            elif board[i-1][red[1]] == '.':

            elif board[i][red[1]] == 'O':
                goal = True
        for i in range(blue[0]-1, 0, -1):
            if
    return goal, board
def solution():
    time = 0
    while True:
        time += 1
        if time > 10:
            time = -1
            break
        dfs