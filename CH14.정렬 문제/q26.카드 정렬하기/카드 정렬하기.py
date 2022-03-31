import sys
import heapq
input = sys.stdin.readline

n = int(input())
card = []

for _ in range(n):
    num = int(input())
    heapq.heappush(card, num)

result = 0
while len(card) >= 2:
    c1 = heapq.heappop(card)
    c2 = heapq.heappop(card)

    sum = c1 + c2
    result += sum
    heapq.heappush(card, sum)

print(result)