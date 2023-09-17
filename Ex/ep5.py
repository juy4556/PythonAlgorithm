from collections import defaultdict


def solution(arr):
    dic = defaultdict(list)
    answer = len(arr)
    result = []
    for i in range(len(arr)):
        if dic[arr[i]]:
            dic[arr[i]].append(i)
            continue
        dic[arr[i]] = [i]

    for value in dic.values():
        if len(value) > 1:
            for i in range(len(value) - 1):
                flag = 0
                for j in range(len(result)):
                    if result[j] and value[i + 1] < result[j][0][0] or value[i] > result[j][-1][1]:
                        result[j].append([value[i], value[i + 1]])
                        flag = 1
                        continue
                if not flag:
                    result.append([[value[i], value[i + 1]]])

    for i in range(len(result)):
        dist = 0
        for j in range(len(result[i])):
            dist += result[i][j][1] - result[i][j][0]
        answer = min(answer, len(arr) - dist)

    return answer


print(solution([1, 2, 10, 2, 1, 2, 1, 10]))
print(solution([1000, 1000, 1000, 1000]))
