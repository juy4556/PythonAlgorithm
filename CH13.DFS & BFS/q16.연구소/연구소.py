import sys
input = sys.stdin.readline
n, m = map(int, input().split()) # n(세로), m(가로)은 3이상 8이하

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

dx = [-1,0,1,0]#상좌하우 순서
dy = [0,1,0,-1]


temp = [[0] * m for _ in range(n)]


def virus_injection(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < m:
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus_injection(nx, ny)


def get_safe():
    safe = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                safe += 1
    return safe

answer = 0
def dfs(count):
    global answer
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = graph[i][j]

        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_injection(i, j)

        answer = max(answer, get_safe())
        return

    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                graph[i][j] = 1
                count += 1
                dfs(count)
                count -= 1
                graph[i][j] = 0

dfs(0)
print(answer)