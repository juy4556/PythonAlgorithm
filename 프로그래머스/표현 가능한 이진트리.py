import math


def get_binary(n, arr):
    a, b = divmod(n, 2)
    arr = str(b) + arr
    if a == 0:
        return arr
    return get_binary(a, arr)


def check_full(arr):
    if math.log2(len(arr) + 1) % 1 == 0:
        return True
    return False


def add_dummy(arr):
    while math.log2(len(arr) + 1) % 1 != 0:
        arr = '0' + arr
    return arr


def divide_and_check(mid, arr):
    left = arr[:mid]
    right = arr[mid + 1:]

    if arr[mid] == '0':
        l, r = left[len(left) // 2], right[len(right) // 2]
        if l == '1' or r == '1':
            return False
    if len(left) >= 2:
        if not divide_and_check(len(left) // 2, left):
            return False
        if not divide_and_check(len(right) // 2, right):
            return False
    return True


def solution(numbers):
    answer = []
    for number in numbers:
        binary = ""
        binary = get_binary(number, binary)
        if not check_full(binary):
            binary = add_dummy(binary)
        if not divide_and_check(len(binary) // 2, binary):
            answer.append(0)
            continue
        answer.append(1)
    return answer


print(solution([7, 42, 5]))
print(solution([63, 111, 95]))
