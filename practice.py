# N = int(input())
# space = []
# dx = [-1, 0, 1, 0]
# dy = [0, 1, 0, -1]
# baby_shark = []
# eatable = []
# result = 0
# for _ in range(N):
#     space.append(list(map(int, input().split())))
#
#
# def dfs(x, y, visited, c):
#     if 0 < space[x][y] < baby_shark[2] and space[x][y] != 9:
#         eatable.append([x, y, c])
#         return
#     for d in range(4):
#         nx = x + dx[d]
#         ny = y + dy[d]
#         if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
#             if space[nx][ny] <= baby_shark[2]:
#                 visited[nx][ny] = 1
#                 dfs(nx, ny, visited, c + 1)
#                 visited[nx][ny] = 0
#
#
# def check_count():
#     global result, eatable
#     eatable = []
#     visited = [[0] * N for _ in range(N)]
#     dfs(baby_shark[0], baby_shark[1], visited, 0)
#
#     if len(eatable) == 0:
#         return False
#
#     elif len(eatable) == 1:
#         space[eatable[0][0]][eatable[0][1]] = 0
#         result += eatable[0][2]
#         space[baby_shark[0]][baby_shark[1]] = 0
#         baby_shark[0], baby_shark[1] = eatable[0][0], eatable[0][1]
#         space[baby_shark[0]][baby_shark[1]] = 9
#
#     elif len(eatable) > 1:
#         min_dist = int(1e9)
#         temp = []
#         for i in range(len(eatable)):
#             if min_dist > eatable[i][2]:
#                 temp = []
#                 min_dist = eatable[i][2]
#                 temp.append([eatable[i][0], eatable[i][1], eatable[i][2]])
#             elif min_dist == eatable[i][2]:
#                 temp.append([eatable[i][0], eatable[i][1], eatable[i][2]])
#
#         if len(temp) > 1:
#             temp.sort(key=lambda x: (x[0], x[1]))
#         space[temp[0][0]][temp[0][1]] = 0
#         space[baby_shark[0]][baby_shark[1]] = 0
#         baby_shark[0], baby_shark[1] = temp[0][0], temp[0][1]
#         result += min_dist
#         space[baby_shark[0]][baby_shark[1]] = 9
#
#     return True
#
#
# def solution():
#     global baby_shark
#     eat_count = 0
#     for i in range(N):
#         for j in range(N):
#             if space[i][j] == 9:
#                 baby_shark = [i, j, 2]
#     while True:
#         if not check_count():
#             break
#         eat_count += 1
#         if eat_count == baby_shark[2]:  # 물고기 먹은 수가 아기상어 크기와 같으면 아기상어의 크기를 1증가
#             baby_shark[2] += 1
#             eat_count = 0
#
#     print(result)
#
#
# solution())