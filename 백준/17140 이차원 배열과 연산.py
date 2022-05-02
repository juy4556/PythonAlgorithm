from collections import defaultdict

r, c, k = map(int, input().split())
A = []
# dic = defaultdict(int)
for _ in range(3):
    A.append(list(map(int, input().split())))


def r_operation(A):
    temp = [[0] for _ in range(len(A))]
    print(A)
    for i in range(len(A)):
        dic = defaultdict(int)
        kind = set()
        for j in range(len(A[0])):
            dic[A[i][j]] += 1
            kind.add(A[i][j])
        for ki in kind:
            temp[i].append((ki, dic[ki]))
        temp[i].sort(key=lambda x: (x[1], x[0]))
    print(temp)


# def c_operation(A):

def solution(A, r, c, k):
    if len(A) <= len(A[0]):
        r_operation(A)
    else:
        c_operation(A)


solution(A, r, c, k)