from collections import deque

if __name__ == "__main__":
    N = int(input())
    tops = list(map(int, input().split()))
    result = [0] * N
    q = deque()
    q.append(0)

    for i in range(1, N):
        while q and tops[i] > tops[q[-1]]:
            q.pop()
        if q and tops[q[-1]] > tops[i]:
            result[i] = q[-1] + 1
        else:
            result[i] = 0
        q.append(i)

    print(*result)
