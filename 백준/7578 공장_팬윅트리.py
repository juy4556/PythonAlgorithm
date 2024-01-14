import sys

input = sys.stdin.readline
if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = {B[i]: i for i in range(N)}
    tree = [0] * (N + 1)


    def update(i, x):
        while i <= N:
            tree[i] += x
            i += i & -i


    def query(i):
        s = 0
        while i:
            s += tree[i]
            i -= i & -i

        return s


    ans = 0
    for i in range(N):
        ans += query(N) - query(B[A[i]])
        update(B[A[i]] + 1, 1)
    print(ans)
