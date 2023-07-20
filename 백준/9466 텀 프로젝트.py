import sys
from collections import deque

sys.setrecursionlimit(100000)


def bfs(start, num, ns):
    q = deque([start])
    visited[start] = 1
    num.append(start)
    ns.add(start)
    while q:
        node = q.popleft()
        next = arr[node] - 1
        if next == start:
            for n in num:
                visited[n] = 1
            return len(num)
        elif next in ns:
            idx = num.index(next)
            for n in num:
                visited[n] = 1
            return len(num) - idx
        if not visited[next]:
            visited[next] = 1
            num.append(next)
            ns.add(next)
            q.append(next)
    return 0


if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        n = int(input())
        arr = list(map(int, input().split()))
        visited = [0] * n
        cycle_count = 0
        for i in range(n):
            if not visited[i]:
                cycle_count += bfs(i, [], set())

        print(n - cycle_count)
