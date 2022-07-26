from collections import defaultdict

dict = defaultdict(list)
dict[1] = [1,2]
dict[1] = [2,3]
dict[2] = [3,4]

for i in range(1, len(dict)+1):
    print(dict[i])
print(dict)