from bisect import bisect_left

if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    dic = {}
    seq = []
    res = []
    for i in range(N):
        dic[A[i]] = i

    for i in range(N):
        seq.append(dic[B[i]])

    res.append(seq[0])
    for i in range(1, N):
        if res[-1] < seq[i]:
            res.append(seq[i])
            continue
        index = bisect_left(res, seq[i])
        res[index] = seq[i]

    print(len(res))
