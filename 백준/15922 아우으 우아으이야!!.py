N = int(input())


def solution():
    lines = []
    result = 0
    for _ in range(N):
        x, y = map(int, input().split())
        lines.append((x, y))
    i = 1
    a, b = lines[0][0], lines[0][1]
    while i < N:
        if b >= lines[i][0]:
            b = max(b, lines[i][1])
        else:
            result += b - a
            a, b = lines[i][0], lines[i][1]
        i += 1
    result += b-a
    print(result)


solution()
