def solution(n, m, fold, cut):
    parent = [[[] for _ in range(m)] for _ in range(n)]
    n_len = n
    m_len = m
    answer = [[1 for _ in range(m)] for _ in range(n)]
    visited = [[0 for _ in range(m)] for _ in range(n)]

    for f in fold:
        if f == 1:
            for j in range(1, m // 2 + 1):
                for i in range(n):
                    parent[i][m // 2 - j].append([i, m // 2 + j - 1])
            m //= 2
        else:
            for i in range(1, n // 2 + 1):
                for j in range(m):
                    parent[n // 2 - i][j].append([n // 2 + i - 1, j])

    for x, y in cut:
        if x - 1 < 0 or x - 1 > n - 1 or y - 1 < 0 or y - 1 > m - 1:
            continue
        answer[x - 1][y - 1] = 0

    for i in range(n):
        for j in range(m):
            print(i, j, parent[i][j], end = ' ')
            visited[i][j] = 1
            for x, y in parent[i][j]:
                if not visited[x][y]:
                    visited[x][y] = 1
                    answer[x][y] = answer[i][j]
        print()

    print("--------------")
    for i in range(n_len):
        for j in range(m_len):
            print(answer[i][j], end=' ')
        print()


solution(8, 6, [1, -1, 1], [[1, 1], [2, 2], [4, 4]])
