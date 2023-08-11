import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    space = []
    start = list(map(int, input().split()))
    maxdp, mindp = start, start
    for i in range(1, N):
        a, b, c = map(int, input().split())
        max_temp = max(maxdp[0], maxdp[1])
        min_temp = min(mindp[0], mindp[1])
        maxdp = [a + max_temp, b + max(max_temp, maxdp[2]), c + max(maxdp[1], maxdp[2])]
        mindp = [a + min_temp, b + min(min_temp, mindp[2]), c + min(mindp[1], mindp[2])]
    print(max(maxdp), min(mindp))
