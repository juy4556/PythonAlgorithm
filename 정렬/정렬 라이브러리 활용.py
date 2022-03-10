array = [1, 0, 2, 6, 3, 7, 3, 8, 2, 6, 8, 4, 2, 3, 5, 6, 4, 2, 3, 7, 9]

result = sorted(array)
print(result)
print(array)

array.sort()
print(array)

arr = [('a',0),('e',5),('c',2)]

def setting(data):
    return data[1]

res = sorted(arr, key=setting)
print(res)
arr.sort(key=setting)
print(arr)