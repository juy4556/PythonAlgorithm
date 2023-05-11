'''
기존 주유소에서 추가로 입력으로 주어지는 초마다 자동차가 에너지를 자가발전함.
1초에 1만큼 움직일 수 있고, 움직이는 데에 1의 에너지를 소비함.
각 주유소에서 1초당 주유할 수 있는 양이 리스트 stations로 주어지고,
주유소 사이에 다리 bridge가 (station크기 -1)크기로 주어짐.
에너지는 최대한 남기면서, 처음 주유소에서 끝 주유소까지 가는 데 걸리는 최소 시간은?
'''
import sys

input = sys.stdin.readline

if __name__ == "__main__":
    N = int(input())
    M = int(input())  # M초마다 에너지 1 자가발전
    bridge = list(map(int, input().split()))
    station = list(map(int, input().split()))
    time, energy = 0, 0
    most_cheap_index = 0

    for i in range(1, len(station) - 1):
        if station[i] < station[most_cheap_index]:
            most_cheap_index = i

    start, end = 0, 1
    while start < most_cheap_index and end <= most_cheap_index:
        time += 1
        if time % M == 0:
            energy += 1

        if station[start] > station[end]:
            end += 1
        else:
            t = 1
            while station[start] * t + energy < sum(bridge[start:end]):
                t += 1
                if (time + t) % M == 0:
                    energy += 1
            time += t
            energy = station[start] * t + energy - sum(bridge[start:end])
            start = end
            end = start + 1

    t = 1
    while station[most_cheap_index] * t + energy < sum(bridge[most_cheap_index:]):
        t += 1
        if (time + t) % M == 0:
            energy += 1
    time += t

    print(time, energy)
