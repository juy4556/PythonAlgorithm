import sys
from collections import defaultdict, deque

sys.setrecursionlimit(10 ** 9)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def dfs(depth, keys, alphabets, all_visited, cost, board):
    if depth == len(keys):
        return
    key = keys.popleft()
    visited = [[0 for _ in range(n)] for _ in range(n)]
    sx, sy = alphabets[key][0]
    ex, ey = alphabets[key][1]
    visited[sx][sy] = 1
    q = deque([[sx, sy]])

    while q:
        x, y = q.popleft()
        if x == ex and y == ey:
            # 최단경로 구하기 위해 역추적
            nq = deque([[ex, ey]])
            while nq:
                a, b = nq.popleft()
                all_visited[a][b] = 1
                for k in range(4):
                    na = a + dx[k]
                    nb = b + dy[k]
                    if na < 0 or na > n - 1 or nb < 0 or nb > n - 1 or not visited[na][nb]:
                        continue
                    if visited[na][nb] == visited[a][b] - 1:
                        cost[a][b].append(2 ** k)
                        cost[na][nb].append(2 ** ((k + 2) % 4))
                        nq.append([na, nb])
                    if a == sx and b == sy:
                        break

            keys.append(key)
            return dfs(depth + 1, keys, alphabets, all_visited, cost, board)

        else:
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1 \
                        or visited[nx][ny] or all_visited[nx][ny] or board[nx][ny] == '#':
                    continue
                visited[nx][ny] = visited[x][y] + 1
                q.append([nx, ny])

    # 모든 알파벳 목표까지 못 간 경우
    keys.append(key)
    all_visited = [[0 for _ in range(n)] for _ in range(n)]
    for values in alphabets.values():
        x1, y1 = values[0]
        all_visited[x1][y1] = 1
    cost = [[[] for _ in range(n)] for _ in range(n)]
    dfs(0, keys, alphabets, all_visited, cost, board)


def solution(n, board):
    alphabet = defaultdict(list)
    keys = set()
    all_visited = [[0 for _ in range(n)] for _ in range(n)]
    cost = [[[] for _ in range(n)] for _ in range(n)]

    for i in range(n):
        for j in range(n):
            if 'a' <= board[i][j] <= 'z':
                if alphabet[board[i][j]]:
                    alphabet[board[i][j]].append([i, j])
                    continue
                alphabet[board[i][j]] = [[i, j]]
                keys.add(board[i][j])

    for k in keys:
        x, y = alphabet[k][0]
        all_visited[x][y] = 1
    keys = deque(list(keys))

    dfs(0, keys, alphabet, all_visited, cost, board)

    for i in range(n):
        for j in range(n):
            print(cost[i][j], end=' ')
        print()


if __name__ == "__main__":
    n = 5
    space = ['.....', '.....', '..a..', '.b.b.', '.cac.']
    # n = 3
    # space = ['..a', '.##', '..a']
    result = [[[] for _ in range(n)] for _ in range(n)]

    solution(n, space)
