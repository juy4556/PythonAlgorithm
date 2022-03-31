import sys
import copy
input = sys.stdin.readline

n, m = map(int, input().split())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
count = 0
max_safe_zone = -1
def check_safezone(graph):
    count = 0
    for i in range(n):
        for j in range(m):
            if graph[i][j] == 0:
                count += 1
    return count

def virus_inject(graph, x, y):
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx < 0 or ny < 0 or nx > n-1 or ny > m-1:
            continue
        if graph[nx][ny] == 0:
            graph[nx][ny] = 2
            virus_inject(graph, nx, ny)


def dfs(count):
    global max_safe_zone
    if count == 3:
        temp = copy.deepcopy(space)
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus_inject(temp, i, j)
        max_safe_zone = max(max_safe_zone, check_safezone(temp))
        return

    for i in range(n):
        for j in range(m):
            if space[i][j] == 0:
                space[i][j] = 1
                count += 1
                dfs(count)
                space[i][j] = 0
                count -= 1

dfs(0)
print(max_safe_zone)