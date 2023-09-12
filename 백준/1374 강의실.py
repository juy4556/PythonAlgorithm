import heapq
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    lectures = []
    rooms = []
    for _ in range(N):
        num, start, end = map(int, input().split())
        heapq.heappush(lectures, [start, end, num])

    while lectures:
        s, e, n = heapq.heappop(lectures)
        if rooms and rooms[0] <= s:
            heapq.heappop(rooms)
            heapq.heappush(rooms, e)
        else:
            heapq.heappush(rooms, e)

    print(len(rooms))
