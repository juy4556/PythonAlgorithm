import sys

input = sys.stdin.readline


def max_dp(max_num):
    max_num[2] = '1'
    max_num[3] = '7'
    for i in range(4, 101):
        max_num[i] = max_num[i - 2] + '1'


def min_dp(min_num):
    min_num[2] = [['1'], 1]
    min_num[3] = [['7'], 7]
    min_num[4] = [['4'], 4]
    min_num[5] = [['2'], 2]
    min_num[6] = [['0'], 6]  # n이 6이면 6
    min_num[7] = [['8'], 8]
    min_num[8] = [['1', '0'], 10]
    min_num[9] = [['1', '8'], 18]
    min_num[10] = [['2', '2'], 22]
    min_num[11] = [['2', '0'], 20]
    min_num[12] = [['2', '8'], 28]
    min_num[13] = [['6', '8'], 68]
    for num in range(14, 101):
        a, b = num // 2, num // 2
        if num & 1:
            b = num // 2 + 1

        while a >= 2 and b <= num - 2:
            arr = sorted(min_num[a][0] + min_num[b][0])
            idx = 0
            length = len(arr)
            while idx < length and arr[idx] == '0':
                idx += 1
            if 0 < idx < length:
                arr = [arr.pop(idx)] + arr
            number = int("".join(arr))
            if number and number < min_num[num][1]:
                _min = number
                min_num[num] = [arr, _min]
            a -= 1
            b += 1


if __name__ == "__main__":
    TC = int(input())
    max_num = ['' for _ in range(101)]
    min_num = [[[], int(1e15)] for _ in range(101)]
    max_dp(max_num)
    min_dp(min_num)
    for tc in range(TC):
        n = int(input())
        maximum = max_num[n]
        minimum = min_num[n][1]
        print(minimum, maximum)
