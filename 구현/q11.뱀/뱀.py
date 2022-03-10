from collections import deque
n = int(input()) # 보드 크기 (2이상 100이하)
k = int(input()) # 사과 개수 (0이상 100이하)
space = [[0] * n for _ in range(n)]
dx = [1,0,-1,0] # 좌하우상
dy = [0,1,0,-1]
direction = 0 # 처음엔 왼쪽향해 움직임

def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

def turn_right():
    global direction
    direction += 1
    if direction == 4:
        direction = 0

for i in range(k):
    a, b = map(int, input().split())
    space[a-1][b-1] = 1

l = int(input()) # 뱀의 방향 변환 횟수 (1이상 100이하)
q = deque()
for i in range(l):
    x, c = input().split()
    q.append((int(x), c))

staying = deque()
staying.append((0, 0))
count = 0
x, y = 0, 0
while 1:
    x += dx[direction]
    y += dy[direction]
    count += 1
    if x >= n or y >= n or x < 0 or y < 0:
        break
    if (x, y) in staying:
        break
    staying.append((x, y))

    if space[y][x] == 1:
        staying.appendleft(staying[0])
        space[y][x] = 0
    if q:
        if q[0][0] == count:
            if q[0][1] == 'D':
                turn_right()
            elif q[0][1] == 'L':
                turn_left()
            q.popleft()
    staying.popleft()


print(count)