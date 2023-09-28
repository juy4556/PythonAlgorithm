import sys

input = sys.stdin.readline


def dfs(x, y, space, visited, count):
    global result
    flag = 0
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx > R - 1 or ny < 0 or ny > C - 1:
            continue
        if visited[space[nx][ny]]:
            continue
        flag = 1
        visited[space[nx][ny]] = 1
        dfs(nx, ny, space, visited, count + 1)
        visited[space[nx][ny]] = 0

    if not flag:
        result = max(result, count)
        return


if __name__ == "__main__":
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    R, C = map(int, input().split())
    space = []
    for _ in range(R):
        space.append(list(map(lambda n: ord(n) - 65, input().rstrip())))
    visited_alphabet = [0 for _ in range(26)]
    visited_alphabet[space[0][0]] = 1
    result = 1

    dfs(0, 0, space, visited_alphabet, 1)
    print(result)
