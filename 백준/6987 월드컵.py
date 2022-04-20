# 한팀과 다른 한팀에 대하여 경기 한 번씩 -> 5*6/2 = 15, 총 15경기
ispossible = [False, False, False, False]


def dfs(teams, order, i, j):
    if i == 6:
        ispossible[order] = True
        return
    elif j == 6:
        dfs(teams, order, i + 1, i + 2)
    if teams[i][0] > 0 and teams[j][2] > 0:
        teams[i][0] -= 1
        teams[j][2] -= 1
        dfs(teams, order, i, j + 1)
        teams[i][0] += 1
        teams[j][2] += 1
    if teams[i][1] > 0 and teams[j][1] > 0:
        teams[i][1] -= 1
        teams[j][1] -= 1
        dfs(teams, order, i, j + 1)
        teams[i][1] += 1
        teams[j][1] += 1
    if teams[i][2] > 0 and teams[j][0] > 0:
        teams[i][2] -= 1
        teams[j][0] -= 1
        dfs(teams, order, i, j + 1)
        teams[i][2] += 1
        teams[j][0] += 1


def solution():
    groups = []
    for i in range(4):
        teams = []
        groups.append(list(map(int, input().split())))
        if sum(groups[i]) != 30:
            continue
        else:
            for j in range(0, 18, 3):
                teams.append([groups[i][j], groups[i][j + 1], groups[i][j + 2]])  # 팀별로 승,무,
            dfs(teams, i, 0, 1)  # i는 몇번째 그룹인지를 나타냄

    for p in ispossible:
        if p:
            print(1, end=' ')
        else:
            print(0, end=' ')


solution()