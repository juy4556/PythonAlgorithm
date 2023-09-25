from collections import deque
import sys

input = sys.stdin.readline


def check(space, array):
    for i in range(N):
        for j in range(N):
            if space[i][j] == 0 and array[i][j] == -1:
                return False
    return True


def spread_virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < 0 or ny < 0 or nx >= N or ny >= N or space[nx][ny] == 1 or visited[nx][ny] >= 0:
            continue  # 리스트 크기를 벗어나거나 벽 또는 이미 방문한 위치에 대해서는 continue
        visited[nx][ny] = visited[x][y] + 1  # 새로운 위치 visited[nx][ny] 값은 이전 visited[x][y]값에서 +1
        q.append([nx, ny])  # 새로운 위치 q에 삽입


def bfs():
    global result, visited, q
    q = deque()
    visited = [[-1] * N for _ in range(N)]  # time을 체크하기 위해 -1로 초기화
    for i in range(M):
        q.append([comb[i][0], comb[i][1]])
        visited[comb[i][0]][comb[i][1]] = 0  # 초기 바이러스 위치는 visited = 0으로 초기화
    time = 0
    while q:
        x, y = q.popleft()
        spread_virus(x, y)  # 바이러스 퍼짐
    if check(space, visited):
        for i in range(N):
            for j in range(N):
                if space[i][j] == 0:  # check를 통과하고 본 위치가 빈칸이었으면 time 초기화
                    time = max(time, visited[i][j])
        result = min(result, time)  # time 중 최소값으로 result 초기화


def comb_three(array, begin):
    if len(comb) == M:
        bfs()  # virus M개 선택되면 bfs
        return
    for i in range(begin, len(array)):
        comb.append(array[i])
        comb_three(array, i + 1)
        comb.pop()


if __name__ == "__main__":
    N, M = map(int, input().split())
    space = []
    for _ in range(N):
        space.append(list(map(int, input().split())))
    comb = []
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    result = int(1e9)
    visited = [[0] * N for _ in range(N)]
    virus = []
    q = deque()
    wall_count = 0

    for i in range(N):
        for j in range(N):
            if space[i][j] == 2:
                virus.append([i, j])  # virus combination 하기 위해 virus에 해당하는 좌표 append
            elif space[i][j] == 1:
                wall_count += 1  # check 용도로 사용

    comb_three(virus, 0)  # combination
    if result == int(1e9):
        print(-1)
    else:
        print(result)
