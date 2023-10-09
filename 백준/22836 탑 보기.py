import sys
from collections import deque

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    buildings = list(map(int, input().split()))
    nearest = [[100001, 100001] for _ in range(N + 1)]
    count = [0 for _ in range(N + 1)]
    stack = []

    for i, v in enumerate(buildings):
        idx = i + 1
        while stack and stack[-1][1] <= v:
            stack.pop()
        count[idx] += len(stack)

        if stack:
            dist = idx - stack[-1][0]
            if dist < nearest[idx][1]:
                nearest[idx] = [stack[-1][0], dist]

        stack.append((idx, v))

    stack = []
    for i, v in reversed(list(enumerate(buildings))):
        idx = i + 1
        while stack and stack[-1][1] <= v:
            stack.pop()
        count[idx] += len(stack)

        if stack:
            dist = stack[-1][0] - idx
            if dist < nearest[idx][1]:
                nearest[idx] = [stack[-1][0], dist]
            elif dist == nearest[idx][1] and stack[-1][0] < nearest[idx][0]:
                nearest[idx][0] = stack[-1][0]

        stack.append((idx, v))

    for i in range(1, N + 1):
        if count[i]:
            print(count[i], nearest[i][0])
        else:
            print(0)
