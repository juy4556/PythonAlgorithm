import heapq
q=[]
heapq.heappush(q, (1,0))
heapq.heappush(q, (0,1))
heapq.heappush(q, (7,2))
heapq.heappush(q, (5,3))
heapq.heappush(q,(11,4))

q1 = q
print(heapq.heappop(q1))
print(heapq.heappop(q1))
print(heapq.heappop(q1))
print(heapq.heappop(q1))
