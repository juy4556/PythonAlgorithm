import sys
from collections import defaultdict

input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
team_head = [0, 0]
team_body = []
team_tail = [0, 0]


def throw_ball(round, n, m):
    get_point_team_idx = -1
    a = round // n
    b = round % n
    if a == 0:
        point = [b, n]
        for team_idx in range(m):
            for value in teams[team_idx]:
                if value[0] == b and value[1] < point[1]:
                    get_point_team_idx = team_idx
                    point = value
        return get_point_team_idx, point
    elif a == 1:
        point = [-1, b]
        for team_idx in range(m):
            for value in teams[team_idx]:
                if value[1] == b and value[0] > point[0]:
                    get_point_team_idx = team_idx
                    point = value
        return get_point_team_idx, point
    elif a == 2:
        point = [b, -1]
        for team_idx in range(m):
            for value in teams[team_idx]:
                if value[0] == n - 1 - b and value[1] > point[1]:
                    get_point_team_idx = team_idx
                    point = value
        return get_point_team_idx, point
    elif a == 3:
        point = [n, b]
        for team_idx in range(m):
            for value in teams[team_idx]:
                if value[1] == n - 1 - b and value[0] < point[0]:
                    get_point_team_idx = team_idx
                    point = value
        return get_point_team_idx, point
    return -1, (-1, -1)


def find_track(x, y, team_idx, visited):
    global n, space, team_head, team_body, team_tail
    if visited[x][y]:
        return
    visited[x][y] = 1
    teams_track[team_idx].append([x, y])
    candidates = []
    if space[x][y] == 1:
        team_head = [x, y]
    elif space[x][y] == 2:
        team_body.append([x, y])
    elif space[x][y] == 3:
        team_tail = [x, y]
    for d in range(4):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx > n - 1 or ny < 0 or ny > n - 1:
            continue

        if space[nx][ny]:
            candidates.append([nx, ny])

    candidates.sort(key=lambda a: space[a[0]][a[1]])
    for a, b in candidates:
        find_track(a, b, team_idx, visited)


def find_team_track(space):
    global n, team_body
    visited = [[0 for _ in range(n)] for _ in range(n)]
    team_idx = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            if space[i][j] == 1:
                team_body = []
                find_track(i, j, team_idx, visited)
                teams[team_idx] = [team_head] + team_body + [team_tail]
                team_idx += 1


def check_rotate_dir(team_idx):
    length = len(teams_track[team_idx])
    for i in range(length):
        if teams[team_idx][0] == teams_track[team_idx][i]:
            if teams[team_idx][1] == teams_track[team_idx][i - 1]:
                return i, 1
            else:
                return i, -1


def move_teams(team_idx):
    start_idx, rotate_dir = check_rotate_dir(team_idx)  # 1이면 시계, -1이면 반시계
    length = len(teams_track[team_idx])
    i = 0
    idx = start_idx + rotate_dir
    while i < len(teams[team_idx]):
        if idx >= length:
            idx %= length
        teams[team_idx][i] = teams_track[team_idx][idx]
        i += 1
        idx += -rotate_dir  # head 따라오도록 진행방향과 반대로


def get_round(num):
    global n
    num %= 4 * n
    return num


def change_head_and_tail(team_idx):
    teams[team_idx].reverse()


def get_point(team_idx, hit_point):
    order = 1
    for value in teams[team_idx]:
        if value == hit_point:
            break
        order += 1
    change_head_and_tail(team_idx)

    return order ** 2


if __name__ == "__main__":
    n, m, k = map(int, input().split())
    teams_track = defaultdict(list)
    teams = defaultdict(list)
    space = []
    points = 0
    for _ in range(n):
        space.append(list(map(int, input().split())))

    find_team_track(space)
    for i in range(k):
        for team_idx in range(m):
            move_teams(team_idx)
        round = get_round(i)
        get_point_team_idx, hit_point = throw_ball(round, n, m)
        if get_point_team_idx >= 0:
            points += get_point(get_point_team_idx, hit_point)

    print(points)
