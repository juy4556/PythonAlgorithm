# 공포도 x인 모험가는 반드시 x명 이상으로 구성한 모험가 그룹에 참여
n = int(input())
array = list(map(int, input().split())) # 각 모험가의 공포도 입력

array.sort()
print(array)
result = 0
count = 0
for i in array:
    count += 1
    if i <= count:
        result += 1
        count = 0


print(result)
