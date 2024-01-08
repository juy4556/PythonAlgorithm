import math
import sys

input = sys.stdin.readline


def query(start, end, node, left, right):
    if left > end or right < start:
        return 0
    if left <= start and end <= right:
        return tree[node]
    mid = (start + end) // 2
    return query(start, mid, node * 2, left, right) + query(mid + 1, end, node * 2 + 1, left, right)


def update(start, end, node, index):
    if index < start or index > end:
        return
    if start == end:
        tree[node] = 1
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index)
    update(mid + 1, end, node * 2 + 1, index)
    tree[node] = tree[node * 2] + tree[node * 2 + 1]
    return


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    B = {B[i]: i for i in range(N)}
    h = int(math.ceil(math.log2(N)))
    size = 1 << (h + 1)
    tree = [0] * size

    result = 0
    for i in range(N):
        result += query(0, N - 1, 1, B[A[i]], N - 1)
        update(0, N - 1, 1, B[A[i]])
    print(result)
