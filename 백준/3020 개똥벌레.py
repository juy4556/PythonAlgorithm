import sys

input = sys.stdin.readline
N, H = map(int, input().split())
down = [0] * (H+1)
up = [0] * (H+1)
for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1
for i in range(H-1,0,-1):
    down[i] += down[i+1]
    up[i] += up[i+1]

min_destroy = N
section_count = 0
for i in range(1, H+1):
    if min_destroy > (down[i] + up[H-i+1]):
        min_destroy = down[i] + up[H-i+1]
        section_count = 1
    elif min_destroy == (down[i] + up[H-i+1]):
        section_count += 1

print(min_destroy, section_count)