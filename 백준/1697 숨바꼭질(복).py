from collections import deque


def bfs(n):
    q = deque([(n, 0)])
    visited[n] = 1
    while q:
        num, cnt = q.popleft()
        if num == K:
            return cnt
        a, b, c = num - 1, num + 1, num * 2
        if a >= 0 and not visited[a]:
            q.append((a, cnt + 1))
            visited[a] = 1
        if b <= 100000 and not visited[b]:
            q.append((b, cnt + 1))
            visited[b] = 1
        if c <= 100000 and not visited[c]:
            q.append((c, cnt + 1))
            visited[c] = 1


if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [0] * 100001
    print(bfs(N))
