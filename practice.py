import heapq
space = []
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0,1,1,1,0,-1,-1,-1]
q = []
for _ in range(4):
    a1, a2, b1, b2, c1, c2, d1, d2 = map(int, input().split())
    space.append([[a1,a2],[b1,b2],[c1,c2],[d1,d2]])
    heapq.heappush(q, [a1, a2])
shark = [0, 0, space[0][0][1]]  # x, y좌표 및 이동방향


def solution():
    for i in range(4):
        for j in range(4):
            heapq.heappush(q, [space[i][j][0], i, j])

    new_q = []
    while q:
        num, x, y = heapq.heappop()


