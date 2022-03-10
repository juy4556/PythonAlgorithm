from itertools import combinations
n, m = map(int, input().split())  # n:2이상 50이하, m:1이상 13이하
space = []
for i in range(n):
    space.append(list(map(int, input().split())))

home = []
chicken = []
for i in range(n):
    for j in range(n):
        if space[i][j] == 1:
            home.append((i+1, j+1))
        elif space[i][j] == 2:
            chicken.append((i+1, j+1))

candidates = combinations(chicken, m)

def get_sum(candidate):
    result = 0
    for hx, hy in home:
        dist = 1e9
        for cx, cy in candidate:
            dist = min(dist, abs(hx-cx)+abs(hy-cy))
        result += dist
    return result

answer = 1e9
for hx, hy in home:
    for candidate in candidates:
        answer = min(answer, get_sum(candidate))
print(answer)