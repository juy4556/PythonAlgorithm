import sys

input = sys.stdin.readline


def sol(a, b, c):
    if b == 1:
        return a % c
    temp = sol(a, b//2, c)
    if b % 2:
        return (temp * temp * a) % c
    else:
        return (temp * temp) % c


if __name__ == "__main__":
    a, b, c = map(int, input().split())
    print(sol(a,b,c))
