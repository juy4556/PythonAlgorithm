if __name__ == "__main__":
    N = int(input())
    x, y = [], []
    for _ in range(N):
        a, b = map(int, input().split())
        x.append(a)
        y.append(b)
    x.append(x[0])
    y.append(y[0])
    c, d = 0, 0
    for i in range(N):
        c += x[i] * y[i+1]
        d += x[i+1] * y[i]

    result = abs(c-d) / 2
    print(result)
