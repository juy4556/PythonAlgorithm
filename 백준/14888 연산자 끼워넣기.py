def calculate(arr):
    result = A[0]
    for i in range(1, len(A)):
        if arr[i - 1] == 0:
            result += A[i]
        elif arr[i - 1] == 1:
            result -= A[i]
        elif arr[i - 1] == 2:
            result *= A[i]
        elif arr[i - 1] == 3:
            if result >= 0:
                result //= A[i]
            else:
                result = (-result // A[i]) * -1
    return result


def dfs(arr):
    global maximum, minimum
    if len(arr) == N - 1:
        result = calculate(arr)
        maximum = max(maximum, result)
        minimum = min(minimum, result)
        return

    for i in range(4):
        if operations[i]:
            arr.append(i)
            operations[i] -= 1
            dfs(arr)
            operations[i] += 1
            arr.pop()


if __name__ == "__main__":
    maximum, minimum = -int(1e9), int(1e9)
    N = int(input())
    A = list(map(int, input().split()))
    operations = list(map(int, input().split()))  # +,-,*,// 순
    dfs([])
    print(maximum)
    print(minimum)
