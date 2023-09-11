import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    works = []
    for _ in range(N):
        T, S = map(int, input().split())
        works.append((T, S))

    works.sort(key=lambda x: x[1])
    time = works[0][1] - works[0][0]
    for i in range(time, -1, -1):
        t = i
        flag = 0
        for j in range(N):
            if t + works[j][0] <= works[j][1]:
                t += works[j][0]
            else:
                flag = 1
                break
        if not flag:
            print(i)
            exit()

    print(-1)
