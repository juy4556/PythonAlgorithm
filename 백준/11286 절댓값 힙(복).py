import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    q = []
    for _ in range(N):
        x = int(input())
        if x:
            heapq.heappush(q, (abs(x), x))
            continue
        if q:
            print(heapq.heappop(q)[1])
            continue
        print(0)
