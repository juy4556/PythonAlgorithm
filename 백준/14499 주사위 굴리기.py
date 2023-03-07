import copy
import sys

input = sys.stdin.readline

# 세로 크기 N, 가로 크기 M (1 ≤ N, M ≤ 20), 주사위를 놓은 곳의 좌표 x, y(0 ≤ x ≤ N-1, 0 ≤ y ≤ M-1),
# 그리고 명령의 개수 K (1 ≤ K ≤ 1,000)
n, m, x, y, k = map(int, input().split())
space = []
for _ in range(n):
    space.append(list(map(int, input().split())))
command = list(map(int, input().split()))
dice = [0 for _ in range(6)]
# 0:front, 1: up, 2: back, 3:bottom, 4: left, 5: right

for cmd in command:
    temp = copy.deepcopy(dice)
    if cmd == 1:
        if y < m - 1:
            y += 1
        else:
            continue
        dice[4] = temp[3]
        dice[1] = temp[4]
        dice[5] = temp[1]
        dice[3] = temp[5]
        if space[x][y] == 0:
            space[x][y] = dice[3]
        else:
            dice[3] = space[x][y]
            space[x][y] = 0
    elif cmd == 2:
        if y >= 1:
            y -= 1
        else:
            continue
        dice[4] = temp[1]
        dice[1] = temp[5]
        dice[5] = temp[3]
        dice[3] = temp[4]
        if space[x][y] == 0:
            space[x][y] = dice[3]
        else:
            dice[3] = space[x][y]
            space[x][y] = 0
    elif cmd == 3:
        if x >= 1:
            x -= 1
        else:
            continue
        dice[0] = temp[3]
        dice[1] = temp[0]
        dice[2] = temp[1]
        dice[3] = temp[2]
        if space[x][y] == 0:
            space[x][y] = dice[3]
        else:
            dice[3] = space[x][y]
            space[x][y] = 0
    elif cmd == 4:
        if x < n - 1:
            x += 1
        else:
            continue
        dice[0] = temp[1]
        dice[1] = temp[2]
        dice[2] = temp[3]
        dice[3] = temp[0]
        if space[x][y] == 0:
            space[x][y] = dice[3]
        else:
            dice[3] = space[x][y]
            space[x][y] = 0

    print(dice[1])
