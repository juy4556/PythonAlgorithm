import sys
from collections import deque

input = sys.stdin.readline


def bfs(n):
    q = deque([[n]])
    visited[n] = 1
    while q:
        arr = q.popleft()
        num = arr[-1]
        visited[num] = 1
        if num == K:
            return arr
        a, b, c = num - 1, num + 1, num * 2
        if a >= 0 and not visited[a]:
            q.append(arr + [a])
        if b <= 100000 and not visited[b]:
            q.append(arr + [b])
        if c <= 100000 and not visited[c]:
            q.append(arr + [c])


if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [0] * 100001
    result = bfs(N)
    print(len(result) - 1)
    print(*result)
