import sys

input = sys.stdin.readline


def dfs(space, visited, x, y):
    global count
    if y == C - 1:
        count += 1
        return True
    for dx, dy in move:
        nx = x + dx
        ny = y + dy
        if nx < 0 or ny < 0 or nx > R - 1 or ny > C - 1:
            continue
        if not visited[nx][ny] and space[nx][ny] == '.':
            visited[nx][ny] = 1
            if dfs(space, visited, nx, ny):
                return True
    return False


if __name__ == "__main__":
    count = 0
    R, C = map(int, input().split())
    space = []
    move = [(-1, 1), (0, 1), (1, 1)]
    for _ in range(R):
        space.append(list(" ".join(input().rstrip()).split()))
    visited = [[0 for _ in range(C)] for _ in range(R)]
    for r in range(R):
        visited[r][0] = 1
        dfs(space, visited, r, 0)
        print(r, count)
        for a in range(R):
            print(visited[a])
    print(count)
