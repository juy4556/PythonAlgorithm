import sys

input = sys.stdin.readline


def divide_and_conquer(arr, length, x, y):
    global result
    num = arr[x][y]
    for i in range(x, x + length):
        for j in range(y, y + length):
            if num != arr[i][j]:
                result += "("
                new_length = length // 2
                for l in range(2):
                    for k in range(2):
                        divide_and_conquer(arr, new_length, x + l * new_length, y + k * new_length)
                result += ")"
                return
    result += str(num)


if __name__ == "__main__":
    N = int(input())
    array = []
    result = ""
    for _ in range(N):
        array.append(list(map(int, ' '.join(input().rstrip()).split(' '))))
    divide_and_conquer(array, N, 0, 0)
    print(result)
