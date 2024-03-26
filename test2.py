import math


def check_dist(x, y, radius):
    return math.sqrt(x ** 2 + y ** 2) <= radius


def solution(direction, radius, X, Y):
    result = 0
    for i in range(len(X)):
        x, y = X[i], Y[i]
        if direction == "U":
            if 0 <= y <= radius and abs(x) <= y:
                if check_dist(x, y, radius):
                    result += 1
        elif direction == "D":
            if -radius <= y <= 0 and abs(x) <= abs(y):
                if check_dist(x, y, radius):
                    result += 1
        elif direction == "L":
            if -radius <= x <= 0 and abs(y) <= abs(x):
                if check_dist(x, y, radius):
                    result += 1
        elif direction == "R":
            if 0 <= x <= radius and abs(y) <= x:
                if check_dist(x, y, radius):
                    result += 1

    return result


print(solution("U", 5, [-1, -2, 4, 1, 3, 0], [5, 4, 3, 3, 1, -1]))
print(solution("D", 10, [0, -3, 2, 0], [-10, -3, -7, -5]))
print(solution("R", 3, [-2, 3], [0, 1]))
