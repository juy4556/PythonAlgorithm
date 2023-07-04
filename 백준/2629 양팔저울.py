def dfs(num, weight):
    if num > n:
        return
    if dp[num][weight]:
        return
    dp[num][weight] = 1

    dfs(num + 1, weight)
    dfs(num + 1, weight + weights[num-1])
    dfs(num + 1, abs(weight - weights[num-1]))


if __name__ == "__main__":
    n = int(input())
    weights = list(map(int, input().split()))
    m = int(input())
    beads = list(map(int, input().split()))
    dp = [[0 for _ in range(n * 500 + 1)] for _ in range(n + 1)]
    result = []

    dfs(0, 0)

    for bead in beads:
        if bead > n * 500:
            result.append("N")
            continue
        if dp[n][bead]:
            result.append("Y")
            continue
        result.append("N")

    print(*result)
