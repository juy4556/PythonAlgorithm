if __name__ == "__main__":
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    arr = [0] * (M+1)
    number = 0
    result = 0
    for a in A:
        number = (number + a) % M
        arr[number] += 1

    for cnt in arr:
        if cnt >= 2:
            result += (cnt * (cnt-1)) // 2
    result += arr[0]

    print(result)
