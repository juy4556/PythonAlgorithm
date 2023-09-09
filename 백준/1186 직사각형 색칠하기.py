import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N, K = map(int, input().split())
    rectangle = []
    width = []
    result = []
    for n in range(N):
        x1, y1, x2, y2 = map(int, input().split())
        rectangle.append((x1, y1, x2, y2))
        width.append([n + 1, (x2 - x1) * (y2 - y1)])
    for i in range(N - 2, -1, -1):
        x1, y1, x2, y2 = rectangle[i]
        for j in range(N - 1, i, -1):
            a1, b1, a2, b2 = rectangle[j]
            if a1 >= x2 or a2 <= x1 or b2 <= y1 or b1 >= y2:
                continue
            x = [x1, x2, a1, a2]
            y = [y1, y2, b1, b2]
            x.sort()
            y.sort()
            x_dif, y_dif = x[2] - x[1], y[2] - y[1]

            width[i][1] -= x_dif * y_dif
    width.sort(key=lambda x: (-x[1], x[0]))
    for i in range(K):
        result.append(width[i][0])

    print(*sorted(result))

'''
2 2
-3 -2 3 2
2 -1 5 4
'''
