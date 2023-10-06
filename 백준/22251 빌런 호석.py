import sys
from collections import defaultdict

input = sys.stdin.readline
if __name__ == "__main__":
    N, K, P, X = map(int, input().split())
    result = 0
    display = [[1, 1, 1, 0, 1, 1, 1], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 1, 1, 0, 1], [1, 0, 1, 1, 0, 1, 1],
               [0, 1, 1, 1, 0, 1, 0], [1, 1, 0, 1, 0, 1, 1], [1, 1, 0, 1, 1, 1, 1], [1, 0, 1, 0, 0, 1, 0],
               [1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 0, 1, 1]]
    nums = [0 for _ in range(K)]
    diff = defaultdict(int)
    for i in range(9):
        for j in range(i + 1, 10):
            count = 0
            for idx in range(7):
                if display[i][idx] != display[j][idx]:
                    count += 1
            diff[(i, j)] = count

    exp = 0
    x = X
    nums[exp] = x % 10
    while x // 10:
        exp += 1
        x //= 10
        nums[exp] = x % 10

    now = [0 for _ in range(K)]
    for stair in range(1, N + 1):
        count = 0
        now[0] += 1
        i = 0
        while now[i] == 10 and i + 1 < K:
            now[i + 1] += 1
            now[i] = 0
            i += 1
        for i in range(K):
            a, b = nums[i], now[i]
            if a == b:
                continue
            elif a < b:
                count += diff[(a, b)]
            else:
                count += diff[(b, a)]
        if count <= P:
            result += 1

    print(result - 1)
