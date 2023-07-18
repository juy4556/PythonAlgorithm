def bin_search1(arr, target):
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
    switches = list(map(int, input().split()))
    lights = list(map(int, input().split()))
    increasing = []
    arr = []
    result = []
    for i in range(N):
        arr.append(lights.index(switches[i]))
    increasing = [[0, arr[0]]]
    seq = [[0, arr[0]]]
    for i in range(1, N):
        if increasing[-1][1] < arr[i]:
            length = len(increasing)
            increasing.append([length, arr[i]])
            seq.append([length, arr[i]])
            continue
        index = bin_search1(increasing, arr[i])
        increasing[index][1] = arr[i]
        seq.append([index, arr[i]])

    temp = []
    index = len(increasing) - 1
    for idx, val in seq[::-1]:
        if idx == index:
            temp.append(val)
            index -= 1
        if index < 0:
            break

    for idx in temp:
        result.append(lights[idx])
    print(len(increasing))
    print(*sorted(result))
