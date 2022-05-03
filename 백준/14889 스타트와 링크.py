N = int(input())
S = []
visited = [False] * N
for _ in range(N):
    S.append(list(map(int, input().split())))

team = []
team1_count = 0
team2_count = 0
result = 1e9


def dfs(begin):
    global team1_count, team2_count, result
    if len(team) == N // 2:
        for i in range(N):
            for j in range(i + 1, N):
                if i == j:
                    continue
                if i in team and j in team:
                    team1_count += (S[i][j] + S[j][i])
                elif i not in team and j not in team:
                    team2_count += (S[i][j] + S[j][i])
        result = min(result, abs(team1_count - team2_count))
        team1_count, team2_count = 0, 0
        return
    for i in range(begin, N):
        team.append(i)
        if 0 not in team:  # 두 팀으로 나누기 위함
            return
        dfs(i + 1)
        team.pop()


def solution():
    dfs(0)
    print(result)


solution()