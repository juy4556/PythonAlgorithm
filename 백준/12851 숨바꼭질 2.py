from collections import deque


def bfs(n):
    global result, count
    q = deque([(n, 0)])
    visited[n] = 1
    while q:
        num, cnt = q.popleft()
        visited[num] = 1
        if cnt > count:
            break
        if num == K:
            result += 1
            count = min(count, cnt)
            continue
        a, b, c = num - 1, num + 1, num * 2
        if a >= 0 and not visited[a]:
            q.append((a, cnt + 1))
        if b <= 100000 and not visited[b]:
            q.append((b, cnt + 1))
        if c <= 100000 and not visited[c]:
            q.append((c, cnt + 1))


if __name__ == "__main__":
    N, K = map(int, input().split())
    visited = [0] * 100001
    result, count = 0, abs(K - N)
    bfs(N)
    print(count)
    print(result)
