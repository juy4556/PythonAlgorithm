import heapq
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    lectures = []
    rooms = []
    room_num = 0
    lecture_room = dict()

    for _ in range(N):
        num, start, end = map(int, input().split())
        heapq.heappush(lectures, [start, end, num])

    while lectures:
        s, e, n = heapq.heappop(lectures)
        if rooms and rooms[0][0] <= s:
            end_time, rn = heapq.heappop(rooms)
            lecture_room[n] = rn
            heapq.heappush(rooms, [e, rn])
        else:
            room_num += 1
            lecture_room[n] = room_num
            heapq.heappush(rooms, [e, room_num])

    print(len(rooms))
    for i in range(1, N + 1):
        print(lecture_room[i])
