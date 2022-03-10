from collections import deque
import sys
import copy
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
time = [0] * (n+1)
indegree = [0] * (n+1)

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0]
    for j in data[1:-1]: # 선수과목들
        graph[j].append(i)
        indegree[i] += 1

result = copy.deepcopy(time)

def topology_sort():
    q = deque()
    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            result[i] = time[i] + result[now]
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(result[i])

topology_sort()