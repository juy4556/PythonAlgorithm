import sys

input = sys.stdin.readline


def count_stars(x_min, y_min):
    count = 0
    for sx, sy in stars:
        if x_min <= sx <= x_min + L and y_min <= sy <= y_min + L:
            count += 1
    return count


if __name__ == "__main__":
    N, M, L, K = map(int, input().split())
    result = 0
    stars = set()
    for k in range(K):
        x, y = map(int, input().split())
        stars.add((x, y))

    for x1, y1 in stars:
        for x2, y2 in stars:
            result = max(result, count_stars(x1, y2))

    print(K - result)
