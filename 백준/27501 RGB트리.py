import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline
rgb = ['R', 'G', 'B']


def dfs(now: int) -> list[int]:
    if visited[now]:
        return dp[now]
    dp[now] = bulbs[now]
    visited[now] = 1
    for node in graph[now]:
        if visited[node]:
            continue
        r, g, b = dfs(node)
        if g > b:
            dp[now][0] += g
        else:
            dp[now][0] += b

        if r > b:
            dp[now][1] += r
        else:
            dp[now][1] += b

        if r > g:
            dp[now][2] += r
        else:
            dp[now][2] += g

    return dp[now]


def get_route(now, color):
    global colors
    if visited[now]:
        return
    visited[now] = 1
    colors[now] = rgb[color]

    for node in graph[now]:
        if visited[node]:
            continue
        r, g, b = dp[node]
        if color == 0:
            if g > b:
                get_route(node, 1)
            else:
                get_route(node, 2)
        elif color == 1:
            if r > b:
                get_route(node, 0)
            else:
                get_route(node, 2)
        elif color == 2:
            if r > g:
                get_route(node, 0)
            else:
                get_route(node, 1)


def print_result():
    max_index = 0
    if dp[1][0] > dp[1][1]:
        if dp[1][0] > dp[1][2]:
            max_index = 0
        else:
            max_index = 2
    else:
        if dp[1][1] > dp[1][2]:
            max_index = 1
        else:
            max_index = 2
    get_route(1, max_index)
    print(dp[1][max_index])
    print("".join(colors))


if __name__ == "__main__":
    N = int(input())
    colors = [""] * (N + 1)
    bulbs = [[]]
    graph = [[] for _ in range(N + 1)]
    visited = [0] * (N + 1)
    dp = [[0, 0, 0] for _ in range(N + 1)]
    for _ in range(N - 1):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)
    for _ in range(N):
        r, g, b = map(int, input().split())
        bulbs.append([r, g, b])

    dfs(1)
    visited = [0] * (N + 1)
    print_result()
