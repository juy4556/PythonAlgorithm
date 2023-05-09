import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, L = map(int, input().split())
    x = list(map(int, input().split()))
    w = list(map(int, input().split()))
    start, end = 0, L

    while end - start >= 0.0000001:
        mid = (start + end) / 2
        left, right = 0, 0
        for i in range(N):
            if mid > x[i]:
                left += w[i] * (mid - x[i])
            else:
                right += w[i] * (x[i] - mid)

        if left > right:
            end = mid
        elif right >= left:
            start = mid

    print(start)
