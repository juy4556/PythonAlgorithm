if __name__ == "__main__":
    N, K = map(int, input().split())
    rank = []
    result = 0
    for _ in range(N):
        rank.append(list(map(int, input().split())))

    rank.sort(key=lambda x: (-x[1], -x[2], -x[3]))
    for i in range(N):
        if K == rank[i][0]:
            result = i + 1
            for j in range(i - 1, -1, -1):
                if rank[i][1:4] == rank[j][1:4]:
                    result -= 1
                else:
                    break
    print(result)
