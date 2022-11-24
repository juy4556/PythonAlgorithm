from collections import deque

dx = [1, 0, 0, -1]  # d,l,r,u
dy = [0, -1, 1, 0]
dir = ['d', 'l', 'r', 'u']


def bfs(n, m, x, y, r, c, k):
    q = deque([[x, y, 0, ""]])
    while q:
        x, y, cnt, directions = q.popleft()
        for d in range(4):
            nx = x + dx[d]
            ny = y + dy[d]
            if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
                continue
            if abs(nx - r) + abs(ny - c) > (k - cnt -1):
                continue
            if nx == r and ny == c and cnt + 1 == k:
                return directions + dir[d]
            q.append([nx, ny, cnt + 1, directions + dir[d]])
            break


def solution(n, m, x, y, r, c, k):
    answer = bfs(n, m, x - 1, y - 1, r - 1, c - 1, k)
    if answer:
        return answer
    return "impossible"


print(solution(3,4,2,3,3,1,5))
print(solution(2,2,1,1,2,2,2))
print(solution(3, 3, 1, 2, 3, 3, 4))
