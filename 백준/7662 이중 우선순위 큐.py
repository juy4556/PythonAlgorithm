import heapq

T = int(input())

for t in range(T):
    min_q, max_q = [], []
    k = int(input())
    visited = [0] * (k + 1)
    for i in range(k):
        op, num = input().split()
        num = int(num)
        if op == 'I':
            heapq.heappush(min_q, (num, i))
            heapq.heappush(max_q, (-num, i))
            visited[i] = 1
        elif op == 'D':
            if num == 1:  # 최댓값 삭제
                while max_q and visited[max_q[0][1]] == 0:
                    heapq.heappop(max_q)
                if max_q:
                    visited[max_q[0][1]] = False
                    heapq.heappop(max_q)
            elif num == -1:  # 최솟값 삭제
                while min_q and visited[min_q[0][1]] == 0:
                    heapq.heappop(min_q)
                if min_q:
                    visited[min_q[0][1]] = False
                    heapq.heappop(min_q)
    while max_q and visited[max_q[0][1]] == 0:
        heapq.heappop(max_q)
    while min_q and visited[min_q[0][1]] == 0:
        heapq.heappop(min_q)
    if max_q and min_q:
        print(-heapq.heappop(max_q)[0], heapq.heappop(min_q)[0])
    else:
        print("EMPTY")
