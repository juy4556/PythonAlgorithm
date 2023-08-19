import heapq
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N, K = map(int, input().split())
    items = []
    baggage = []
    q = []
    q1 = []
    result = 0
    for _ in range(N):
        M, V = map(int, input().split())
        heapq.heappush(q, [M, V])

    for _ in range(K):
        C = int(input())
        baggage.append(C)
    baggage.sort()

    for b in baggage:
        while q:
            m, v = heapq.heappop(q)
            if b >= m:
                heapq.heappush(q1, -v)
            else:
                heapq.heappush(q, [m, v])
                break
        if q1:
            result += -heapq.heappop(q1)

    print(result)
