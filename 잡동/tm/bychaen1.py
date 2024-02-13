'''
x: 기지국 원 중심 x좌표
y: 기지국 원 중심 y좌표
r: 각 기지국이 커버하는 영역의 반지름
v: 난수 배열(앞에서 부터 2개씩 순서대로 사용해 시뮬레이션에 사용할 점의 좌표로 활용)
몬테카를로 법칙
직사각형 안 위치를 특정하기 위한 좌표 변환 (x,y) -> (l+x%(r-l), b+y%(t-b))
기지국 영역 면적 = k(비율) * (r-l) * (t-b)
'''
import math


def check_circle(x, y, cx, cy, r):
    if math.pow(r, 2) >= math.pow(cx - x, 2) + math.pow(cy - y, 2):
        return True
    return False


def solution(x, y, r, v):
    lx, by, rx, ty = 50000, 50000, 0, 0
    k = 0  # 비율
    count = 0
    result = 0
    for i in range(len(x)):
        lx = min(rx, x[i] - r[i])
        by = min(by, y[i] - r[i])
        rx = max(lx, x[i] + r[i])
        ty = max(ty, y[i] + r[i])

    for i in range(0, len(v), 2):
        nx = lx + v[i] % (rx - lx)
        ny = by + v[i + 1] % (ty - by)
        for j in range(len(x)):
            if check_circle(nx, ny, x[j], y[j], r[j]):
                count += 1
                break
    count /= len(v) // 2
    result = int(count * (rx - lx) * (ty - by))
    print(result)


solution([5], [5], [5], [92, 83, 14, 45, 66, 37, 28, 9, 10, 81])
solution([3, 4], [3, 5], [2, 3], [12, 83, 54, 35, 686, 337, 258, 95, 170, 831, 8, 15])
