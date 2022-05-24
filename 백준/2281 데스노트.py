n, m = map(int, input().split()) # n은 사람 수, m은 가로 폭 길이
name = []
array = [[]]
for _ in range(n):
    name.append(int(input())) # 이름 길이 입력

for i in range(n):
    if sum(array[-1]) + len(array[-1]) + name[i] <= m:
        array[-1].append(name[i])
    else:
        array.append([name[i]])
print(array)
for i in range(len(array)-2): # 마지막 배열은 생각 X
    while pow(m - (sum(array[i]) + len(array[i]) - 1), 2) + pow(m - (sum(array[i+1]) + len(array[i+1]) - 1), 2) > \
            pow(m - (sum(array[i]) - array[i][-1] + len(array[i]) - 2), 2) \
            + pow(m - (sum(array[i+1]) + array[i][-1] + len(array[i+1])), 2) \
            and array[i][-1] + sum(array[i+1]) + len(array[i+1]) <= m:
        array[i+1].insert(0, array[i].pop())
print(array)
result = 0
for i in range(len(array)-1):
    result += pow(m - (sum(array[i]) + len(array[i]) - 1), 2)
print(result)