from bisect import bisect_left
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, H = map(int, input().split())
    heights = []
    top = []
    bottom = []
    start, end = 0, N

    for n in range(N):
        if n % 2:
            top.append(int(input()))
            continue
        bottom.append(int(input()))

    top.sort()
    bottom.sort()

    minimum = 200001
    sections = H
    for h in range(1, H + 1):
        t, b = bisect_left(top, H + 1 - h), bisect_left(bottom, h)
        count = N - t - b
        if count < minimum:
            minimum = count
            sections = 1
        elif count == minimum:
            sections += 1

    print(minimum, sections)
