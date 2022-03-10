import heapq


def solution(food_times, k):
    q = []
    if sum(food_times) <= k:  # k시간 내에 다 먹을 수 있으면
        return -1
    for i in range(len(food_times)):
        heapq.heappush(q, (food_times[i], i + 1))

    eat_time = 0
    previous_time = 0
    length = len(food_times)
    while eat_time + ((q[0][0] - previous_time) * length) < k:
        now = heapq.heappop(q)[0]
        eat_time += (now - previous_time) * length
        previous_time = now
        length -= 1
    result = sorted(q, key= lambda x: x[1])
    return result[(k-eat_time)%length][1]