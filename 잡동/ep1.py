def solution(ax, ay, bx, by, square):
    result = abs(ax - bx) + abs(ay - by)

    square[0], square[1], square[2], square[3]
    x = [square[0][0], square[1][0]]
    y = [square[1][1], square[2][1]]
    a_min = 4001
    b_min = 4001

    for a in x:
        for b in range(y[0], y[1] + 1):
            a_min = min(a_min, abs(ax - a) + abs(ay - b))
            b_min = min(b_min, abs(bx - a) + abs(by - b))

    for a in range(x[0] + 1, x[1]):
        for b in y:
            a_min = min(a_min, abs(ax - a) + abs(ay - b))
            b_min = min(b_min, abs(bx - a) + abs(by - b))

    result = min(result, a_min + b_min)
    return result

    print(result)


solution(-4, 1, 2, 4, [[-2, 2], [1, 2], [1, 5], [-2, 5]])
solution(2, 3, 5, 2, [[1, 1], [6, 1], [6, 5], [1, 5]])
solution(2, 3, -2, 4, [[1, -2], [4, -2], [4, 1], [1, 1]])
solution(1, 2, -2, -2, [[-2, -2], [2, -2], [2, 2], [-2, 2]])
