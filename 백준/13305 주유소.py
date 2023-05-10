import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    bridge = list(map(int, input().split()))
    station = list(map(int, input().split()))
    pay = 0
    most_cheap = 0

    for i in range(1, len(station) - 1):
        if station[i] < station[most_cheap]:
            most_cheap = i

    pay += station[most_cheap] * sum(bridge[most_cheap:])

    start, end = 0, 1
    while start < most_cheap and end <= most_cheap:
        if station[start] < station[end]:
            end += 1
        else:
            pay += station[start] * sum(bridge[start:end])
            start = end
            end = start + 1

    print(pay)
