def bin_search(arr, target, start, end):
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
    arr = [[0, A[0]]]  # 수열의 인덱스와 값을 함께 리스트에 저장
    result = [[0, A[0]]]

    for i in range(1, N):
        if arr[-1][1] < A[i]:  # 수열 값이 리스트 마지막 요소의 값보다 크면 추가
            arr.append([i, A[i]])
            result = arr[::]
            continue
        index = bin_search(arr, A[i], 0, len(arr) - 1)
        if arr[index][1] > A[i]:  # 이중탐색으로 얻은 리스트의 값이 수열의 값보다 클 때만 리스트 요소 초기화
            arr[index] = [i, A[i]]

    result = [[-1, -int(1e9)]] + result

    for i in range(len(result) - 1):
        if result[i][0] > result[i + 1][0]:  # result 리스트에 인덱스[0]의 값(수열 요소값)이 다음 인덱스의 값보다 클 때
            for j in range(result[i - 1][0] + 1, result[i + 1][0]):  # 이전 인덱스의 요소 값 ~ 다음 인덱스 요소 값 사이에서
                if A[j] < result[i + 1][1]:  # 다음 인덱스의 값보다 작은 수열 값 찾아서 초기화
                    result[i] = [j, A[j]]

    print(len(result) - 1)
    print(*[result[i][1] for i in range(1, len(result))])
