from typing import List


def fire_spread(space, x, y, t, n):
    for dx in range(-t, t + 1):
        for dy in range(-t, t + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                space[nx][ny] += 1


def ice_spread(space, x, y, t, n):
    for dx in range(-t, t + 1):
        yt = abs(abs(dx) - t)
        for dy in range(-yt, yt + 1):
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < n:
                space[nx][ny] -= 1


def solution(n: int, m: int, fires: List[List[int]], ices: List[List[int]]) -> List[List[int]]:
    space = [[0 for _ in range(n)] for _ in range(n)]
    t = 0
    while t < m:
        t += 1
        for i in range(len(fires)):
            x, y = fires[i][0] - 1, fires[i][1] - 1
            fire_spread(space, x, y, t, n)
        for j in range(len(ices)):
            x, y = ices[j][0] - 1, ices[j][1] - 1
            ice_spread(space, x, y, t, n)

    return space
