import sys

input = sys.stdin.readline


def check(n):
    for i in range(n):
        if rows[n] == rows[i] or abs(rows[n] - rows[i]) == abs(n - i):
            return 0
    return 1


def dfs(n):
    global result
    if n == N:
        result += 1
        return

    for i in range(N):
        rows[n] = i
        if check(n):
            dfs(n + 1)


if __name__ == "__main__":
    N = int(input())
    rows = [0 for _ in range(N)]
    result = 0
    dfs(0)
    print(result)
