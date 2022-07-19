graph = [[1], [2], [3], [4], [5], [6, 21], [7], [8], [9], [10], [11, 25], [12], [13], [14], [15], [16, 27], [17],
         [18], [19], [20], [32], [22], [23], [24], [30], [26], [24], [28], [29], [24], [31], [20], [32]]
scores = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 13, 16, 19, 25, 22, 24, 28, 27,
          26, 30, 35, 0]
dice = list(map(int, input().split()))
result = 0


def dfs(depth, total, horses):
    global result
    if depth == 10:
        result = max(result, total)
        return

    for i in range(4):
        temp = horses[i]
        if len(graph[temp]) == 2:
            temp = graph[temp][1]
        elif len(graph[temp]) == 1:
            temp = graph[temp][0]
        for j in range(1, dice[depth]):
            temp = graph[temp][0]
        if temp == 32 or (temp < 32 and temp not in horses):
            tmp = horses[i]
            horses[i] = temp
            dfs(depth + 1, total + scores[temp], horses)
            horses[i] = tmp


dfs(0, 0, [0, 0, 0, 0])
print(result)