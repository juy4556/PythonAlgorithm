import sys

input = sys.stdin.readline


def check_sum(X, mid, K):
    num = 0
    for i in range(len(X)):
        if X[i] < mid:
            num += mid - X[i]
        if num > K:
            return 1
    return 0


def bin_search(X, K):
    start, end = 0, X[-1] + K
    while start <= end:
        mid = (start + end) // 2
        if check_sum(X, mid, K):
            end = mid - 1
            continue
        start = mid + 1
    return end


if __name__ == "__main__":
    N, K = map(int, input().split())
    X = []
    for _ in range(N):
        X.append(int(input()))
    X.sort()
    print(bin_search(X, K))
