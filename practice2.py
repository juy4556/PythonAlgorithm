from collections import defaultdict

if __name__ == "__main__":
    N = 7
    T = 5
    apples = [[2, 1], [2, 7], [3, 2], [3, 3], [3, 6], [4, 1], [4, 3], [4, 7]]
    dp = [[[0, 0] for _ in range(N + 1)] for _ in range(T + 1)]
    positions = defaultdict(list)
    for h, c in apples:
        positions[h].append(c)
    apples.sort(key=lambda x: x[0])
    first_height = apples[0][0]
    available_move1 = set([i for i in range(1, first_height + 1)])
    available_move2 = set([i for i in range(N, N - first_height, -1)])
    for p in positions[first_height]:
        if p in available_move1:
            dp[first_height][p] = [1, 1]
        elif p in available_move2:
            dp[first_height][p] = [1, 2]
    for i in range(first_height + 1, T + 1):
        dp[i] = dp[i - 1][:]
        if i in positions.keys():
            for p in positions[i]:
                if p == 1:
                    if dp[i - 1][p][0] > dp[i - 1][p + 1][0]:
                        dp[i][p] = [dp[i - 1][p][0] + 1, dp[i - 1][p][1]]
                    else:
                        dp[i][p] = [dp[i - 1][p + 1][0] + 1, dp[i - 1][p + 1][1]]
                elif p == N:
                    if dp[i - 1][p][0] > dp[i - 1][p - 1][0]:
                        dp[i][p] = [dp[i - 1][p][0] + 1, dp[i - 1][p][1]]
                    else:
                        dp[i][p] = [dp[i - 1][p - 1][0] + 1, dp[i - 1][p - 1][1]]
                else:
                    if dp[i - 1][p][0] > dp[i - 1][p - 1][0] and dp[i - 1][p][0] > dp[i - 1][p + 1][0]:
                        dp[i][p] = [dp[i - 1][p][0] + 1, dp[i - 1][p][1]]
                    elif dp[i - 1][p - 1][0] > dp[i - 1][p][0] and dp[i - 1][p - 1][0] > dp[i - 1][p + 1][0]:
                        dp[i][p] = [dp[i - 1][p - 1][0] + 1, dp[i - 1][p - 1][1]]
                    else:
                        dp[i][p] = [dp[i - 1][p + 1][0] + 1, dp[i - 1][p + 1][1]]
    a, b = 0, 0
    for i in range(1, N + 1):
        if dp[T][i][1] == 1:
            a = max(a, dp[T][i][0])
        elif dp[T][i][1] == 2:
            b = max(b, dp[T][i][0])
    print(a + b)
