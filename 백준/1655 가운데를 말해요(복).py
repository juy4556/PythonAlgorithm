import heapq
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    left = []
    right = []
    result = []
    for _ in range(N):
        n = int(input())
        if len(left) == len(right):
            heapq.heappush(left, -n)
        else:
            heapq.heappush(right, n)

        if right and -left[0] > right[0]:
            l = -heapq.heappop(left)
            r = heapq.heappop(right)
            heapq.heappush(left, -r)
            heapq.heappush(right, l)

        print(-left[0])
