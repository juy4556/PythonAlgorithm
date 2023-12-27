import sys
from collections import deque

'''
동전 합 k
사용한 동전의 개수 최소
각 동전은 몇 개라도 사용 가능
사용한 동전 구성 같은데 순서만 다르면 같은 경우
1 <= n <= 100
1 <= k <= 10000
1 <= 동전 가치 <= 100000
'''
input = sys.stdin.readline
if __name__ == "__main__":
    n, k = map(int, input().split())
    arr = set(int(input()) for _ in range(n))
    coins = []
    q = deque()
    visited = [0 for _ in range(k + 1)]
    for num in arr:
        if num <= k:
            coins.append(num)
    for coin in coins:
        if coin == k:
            print(1)
            exit(0)
        visited[coin] = 1

    for i, v in enumerate(coins):
        q.append((i, v))
    coins_length = len(coins)
    count = 1
    while q:
        for i in range(len(q)):
            idx, total_value = q.popleft()

            for j in range(idx, coins_length):
                total = total_value + coins[j]
                if total == k:
                    print(count + 1)
                    exit(0)
                elif total < k and not visited[total]:
                    visited[total] = 1
                    q.append((j, total))
        count += 1

    print(-1)
