def bin_search(arr, target):
    start, end = 0, len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid][1] >= target:
            end = mid - 1
            continue
        start = mid + 1
    return start


if __name__ == "__main__":
    N = int(input())
    A = list(map(int, input().split()))
    seq = [[0, A[0]]]
    res = [[0, A[0]]]
    result = []
    for i in range(1, len(A)):
        if seq[-1][1] < A[i]:
            length = len(seq)
            seq.append([length, A[i]])
            res.append([length, A[i]])
            continue
        index = bin_search(seq, A[i])
        seq[index][1] = A[i]
        res.append([index, A[i]])

    index = len(seq) - 1
    for idx, val in res[::-1]:
        if idx == index:
            result.append(val)
            index -= 1
        if index < 0:
            break
    print(len(seq))
    print(*result[::-1])
