import sys

input = sys.stdin.readline
answer = []


def dfs(arr, n):
    global answer
    if sum(arr) >= n:
        if sum(arr) == n:
            answer.append(list(arr))
        return

    for i in range(1, 4):
        arr.append(i)
        dfs(arr, n)
        arr.pop()


if __name__ == "__main__":
    n, k = map(int, input().split())
    dfs([], n)
    if k <= len(answer):
        print("+".join(str(s) for s in answer[k - 1]))
    else:
        print(-1)
