# 계수 정렬은 모든 데이터가 양의 정수이고, 원소의 최소, 최대 값의 크기 차이가 크지 않을 때 효율적
array = [1, 0, 2, 6, 3, 7, 3, 8, 2, 6, 8, 4, 2, 3, 5, 6, 4, 2, 3, 7, 9]
count = [0] * (max(array)+1) # 1더해주는 이유는 min이 0이기 때문(0포함이기때문)

for i in range(len(array)):
    count[array[i]] += 1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=" ")