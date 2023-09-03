import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    cranes = list(map(int, input().split()))
    M = int(input())
    boxes = list(map(int, input().split()))
    # crane, boxes asc 정렬
    cranes.sort()
    boxes.sort()
    # 가져갔는지 여부. 가져갔으면 1, 아니면 0
    take = [0 for _ in range(M)]
    # 각 크레인의 인덱스
    points = [0] * N
    time = 0

    # 박스 최대 무게를 옮길 크레인 없으면 -1출력 후 종료
    if cranes[-1] < boxes[-1]:
        print(-1)
        exit()

    # a는 크레인 마지막 인덱스, b는 박스 마지막 인덱스
    # 마지막 인덱스부터 크레인 가능 무게 >= 박스 무게면 인덱싱
    # 인덱싱은 point 리스트 사용함
    a, b = N - 1, M - 1
    while a >= 0 and b >= 0:
        if cranes[a] >= boxes[b]:
            points[a] = b
            a -= 1
        b -= 1

    # 아직 take하지 않은게(0) 있으면 반복
    while take.count(0) > 0:
        # 마지막 포인트부터 take하지 않은게 있을 때까지 인덱스 변경
        for p in range(N - 1, -1, -1):
            while points[p] > 0 and take[points[p]]:
                points[p] -= 1
            # 해당 포인터에 해당하는 인덱스가 take 안됐으면 take
            if not take[points[p]] and cranes[p] >= boxes[points[p]]:
                take[points[p]] = 1
        time += 1

    print(time)
