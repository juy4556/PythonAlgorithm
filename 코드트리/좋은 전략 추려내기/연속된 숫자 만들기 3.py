arr = list(map(int, input().split()))
arr.sort()

if arr[1] - arr[0] > arr[2] - arr[1]:
    print(arr[1] - arr[0] - 1)
elif arr[2] - arr[1] > arr[1] - arr[0]:
    print(arr[2] - arr[1] - 1)
else:
    print(0)
