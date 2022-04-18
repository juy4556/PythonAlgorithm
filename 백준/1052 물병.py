import sys
input = sys.stdin.readline
N, K = map(int, input().split())

i = 0
while True:
    if bin(N+i).count('1') <= K:
        print(i)
        break
    else:
        i += 1