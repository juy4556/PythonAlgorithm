import sys
from heapq import heappush, heappop

input = sys.stdin.readline


def dfs(parents, cur):
    if not parents[cur]:
        return

    q = []
    for next in parents[cur]:
        dfs(parents, next)
        heappush(q, -dp[next])

    order = 1
    while q:
        temp = heappop(q)
        depth = -temp
        dp[cur] = max(dp[cur], depth + order)
        order += 1


if __name__ == "__main__":
    N = int(input())
    bosses = list(map(int, input().split()))
    parents = [[] for _ in range(N)]
    dp = [0 for _ in range(N)]
    for i in range(1, N):
        parents[bosses[i]].append(i)

    dfs(parents, 0)
    print(dp[0])
