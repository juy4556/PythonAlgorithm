def dfs(n, begin, arr):
    global result
    if len(arr) == n // 2:
        team1, team2 = 0, 0
        for i in range(N):
            for j in range(i + 1, N):
                if i in arr and j in arr:
                    team1 += (S[i][j] + S[j][i])
                elif i not in arr and j not in arr:
                    team2 += (S[i][j] + S[j][i])
        result = min(result, abs(team1 - team2))
        return

    for i in range(begin, n):
        arr.append(i)
        if 0 not in arr:
            return
        dfs(n, i + 1, arr)
        arr.pop()


if __name__ == "__main__":
    N = int(input())
    S = []
    result = int(1e9)
    for _ in range(N):
        S.append(list(map(int, input().split())))

    dfs(N, 0, [])
    print(result)
