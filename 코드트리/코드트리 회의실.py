def bin_search(rooms, target):
    left = 0
    right = len(rooms) - 1
    while left <= right:
        mid = (left + right) // 2
        if rooms[mid] <= target:
            left = mid + 1
            continue
        right = mid - 1
    return right


N, M = map(int, input().split())
rooms = [[-1, -1] for _ in range(M)]  # 첫번째 요소: endTime, 두번째 요소: 인덱스
schedules = []
q = []
for i in range(N):
    s, e = map(int, input().split())
    schedules.append((s, e))

schedules.sort(key=lambda x: (x[0], x[1]))

count = 0
print("schedules:", schedules)
for i in range(N):
    s, e = schedules[i]
    print(s, e, rooms)
    while rooms and s >= rooms[-1]:
        rooms.pop()
    if len(rooms) < M:
        rooms.append(e)
        rooms.sort(reverse=True)
    else:
        idx = bin_search(rooms, e) - 1
        print("here", idx)
        if idx >= 0:
            rooms[idx] = e
        count += 1

print(N - count)
