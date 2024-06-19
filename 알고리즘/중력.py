arr = [[0, 1, 0], [1, 0, 1], [0, 1, 0], [0, 0, 1], [0, 1, 0]]

print("기존")
for i in range(len(arr)):
    print(arr[i])


def gravity():
    n = len(arr)
    m = len(arr[0])
    for i in range(n - 1):
        for j in range(m):
            k = i
            while arr[k][j] == 1 and arr[k + 1][j] == 0:
                arr[k][j], arr[k + 1][j] = 0, 1
                k -= 1


gravity()

print("변화")
for i in range(len(arr)):
    print(arr[i])
