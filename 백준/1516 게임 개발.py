import heapq
import sys

input = sys.stdin.readline


def topology_sort():
    result = building_time[:]
    q = []
    for i in range(1, N + 1):
        if indegree[i] == 0:
            heapq.heappush(q, (building_time[i], i))

    while q:
        time, now = heapq.heappop(q)
        for node in graph[now]:
            indegree[node] -= 1
            result[node] = time + building_time[node]
            if indegree[node] == 0:
                heapq.heappush(q, (result[node], node))

    return result


if __name__ == "__main__":
    N = int(input())
    graph = [[] for _ in range(N + 1)]
    indegree = [0 for _ in range(N + 1)]
    building_time = [0]
    for i in range(1, N + 1):
        arr = list(map(int, input().split()))
        building_time.append(arr[0])

        for j in range(1, len(arr) - 1):
            graph[arr[j]].append(i)
            indegree[i] += 1
    result = topology_sort()
    for i in range(1, N + 1):
        print(result[i])
