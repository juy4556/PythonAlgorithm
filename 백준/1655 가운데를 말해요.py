import heapq

N = int(input())
left, right = [], []
result = []
for n in range(N):
    if len(left) == len(right):
        heapq.heappush(left, -int(input()))
    elif len(left) != len(right):
        heapq.heappush(right, int(input()))

    if right and -left[0] > right[0]:
        lmax = -heapq.heappop(left)
        rmin = heapq.heappop(right)
        heapq.heappush(left, -rmin)
        heapq.heappush(right, lmax)
    result.append(-left[0])
for res in result:
    print(res)