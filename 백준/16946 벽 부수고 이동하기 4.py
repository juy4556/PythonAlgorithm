from collections import deque, defaultdict
import sys

input = sys.stdin.readline


def bfs(x, y, visited, n):
    q = deque([[x, y]])
    visited[x][y] = n
    count = 1
    while q:
        x, y = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or visited[nx][ny]:
                continue
            if space[nx][ny] == '0':
                q.append([nx, ny])
                visited[nx][ny] = n
                count += 1
    group_count[n] = count


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    N, M = map(int, input().split())
    space = []
    for _ in range(N):
        space.append(input().rstrip())
    result = [[0 for _ in range(M)] for _ in range(N)]
    visited = [[0 for _ in range(M)] for _ in range(N)]
    group_count = defaultdict(int)
    group_num = 1

    for i in range(N):
        for j in range(M):
            if space[i][j] == '0' and not visited[i][j]:
                bfs(i, j, visited, group_num)
                group_num += 1
    for i in range(N):
        for j in range(M):
            if space[i][j] == '1':
                count = 1
                visited_group = set()
                for d in range(4):
                    nx = i + dx[d]
                    ny = j + dy[d]
                    if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1 or space[nx][ny] == '1':
                        continue
                    group_number = visited[nx][ny]
                    if group_number not in visited_group:
                        count += group_count[group_number]
                        visited_group.add(group_number)
                result[i][j] = count % 10

    for i in range(N):
        print("".join(map(str, result[i])))
