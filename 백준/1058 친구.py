import sys

input = sys.stdin.readline
N = int(input())
arr = []
graph = [[0] * N for _ in range(N)]


def solution(N):
    result = 0
    for _ in range(N):
        arr.append(input().rstrip())

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if i == j:
                    continue
                if arr[i][j] == "Y" or (arr[i][k] == "Y" and arr[k][j] == "Y"):
                    graph[i][j] = 1
    for i in range(N):
        result = max(result, sum(graph[i]))
    print(result)


solution(N)
