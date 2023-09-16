from collections import deque


def solution(N, K, charges):
    stations = [0 for _ in range(N)]
    q = deque(charges)
    time = 0
    result = []
    while True:
        min_charge = 100001
        for i in range(N):
            if stations[i] == 0:
                stations[i] = q.popleft()
                if not q:
                    result = [i + 1, time + stations[i]]
                    break
            if stations[i]:
                min_charge = min(min_charge, stations[i])

        for i in range(N):
            if stations[i]:
                stations[i] -= min_charge
        time += min_charge

        if not q:
            break

    return result
