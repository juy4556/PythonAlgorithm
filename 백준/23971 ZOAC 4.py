if __name__ == "__main__":
    H, W, N, M = map(int, input().split())
    x, y = 0, 0
    for i in range(0, H, N + 1):
        x += 1

    for i in range(0, W, M + 1):
        y += 1

    print(x * y)
