import heapq
q=[]
heapq.heappush(q, (1,0))
heapq.heappush(q, (0,1))
heapq.heappush(q, (7,2))
heapq.heappush(q, (5,3))
heapq.heappush(q,(11,4))
visited = [0] * 5
visited[2] = 1
while q and visited[q[0][1]] == 0:
    heapq.heappop(q)
if q:
    heapq.heappop(q)

print(q)