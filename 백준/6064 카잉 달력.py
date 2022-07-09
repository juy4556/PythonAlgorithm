import sys

input = sys.stdin.readline

if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        M, N, x, y = map(int, input().split())
        while x < M * N:
            if (x - y) % N == 0:
                break
            x += M
        if x > M * N:
            print(-1)
            continue
        print(x)
