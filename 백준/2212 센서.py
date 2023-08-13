if __name__ == "__main__":
    N = int(input())
    K = int(input())
    sensor = list(map(int, input().split()))
    sensor.sort()

    if K >= N:
        print(0)
        exit()
    interval = [sensor[i + 1] - sensor[i] for i in range(N - 1)]
    interval.sort()
    for i in range(K - 1):
        interval.pop()

    print(sum(interval))
