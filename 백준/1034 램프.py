import sys
input = sys.stdin.readline

def solution():
    N, M = map(int, input().split())
    space = []
    for _ in range(N):
        space.append(list(input().rstrip()))
    K = int(input())
    result = 0
    for i in range(N):
        cnt = 0
        if space[i].count('0') <= K and space[i].count('0') % 2 == K % 2:
            for j in range(N):
                if space[i] == space[j]:
                    cnt += 1
        result = max(result, cnt)
    print(result)

solution()