import sys
from bisect import bisect_left

input = sys.stdin.readline
if __name__ == "__main__":
    n = int(input())
    boxes = list(map(int, input().split()))
    longest = [boxes[0]]

    for i in range(1, n):
        if longest[-1] < boxes[i]:
            longest.append(boxes[i])
        else:
            idx = bisect_left(longest, boxes[i])
            longest[idx] = boxes[i]
    print(len(longest))
