from collections import defaultdict
arr = [['A', 10], ['B', 20], ['C', 30], ['A', 40], ['D', 50], ['A', 40]]
dic = defaultdict(list)
for i in range(len(arr)):
    dic[arr[i][0]].append([i, arr[i][1]])

print(dic['A'])

