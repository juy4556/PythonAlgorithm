n = int(input())
array = []

for _ in range(n):
    array.append(int(input()))

array.sort(reverse=True)


def solution(array):
    if n == 1:
        return array[0]
    result = 0
    index1, index2 = 0, len(array) - 1

    # 곱셈해야할 때
    for j in range(len(array) - 1, 0, -2):
        if array[j] < 0 and array[j - 1] <= 0:
            result += (array[j] * array[j - 1])
            index2 = j - 2
        else:
            index2 = j
            break

    for i in range(0, len(array) - 1, 2):
        if array[i] > 1 and array[i + 1] > 1:
            result += (array[i] * array[i + 1])
            index1 = i + 2
        else:
            index1 = i
            break

    if index1 > index2:
        return result
    else:
        for i in range(index1, index2 + 1):
            result += array[i]
    return result


print(solution(array))
