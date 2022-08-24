arr = [1, 2, 3, 4, 5]
arr1 = [6, 7, 8, 9, 10]
arr[1], arr[4] = arr[4], 0
print(arr)

arr, arr1 = arr1, arr
print(arr)
print(arr1)

a, b = 1, 2
for i in range(4):
    print(a+i*2,b+i*2)