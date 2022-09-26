from collections import defaultdict

dic = defaultdict(list)


def solution(queries):
    num = set()
    answer = 0
    for i in range(len(queries)):
        index, value = queries[i][0], queries[i][1]
        if index not in num:
            num.add(index)
            n = 1
            while n < queries[i][1]:
                n *= 2
            dic[index] = [value, n]
        else:
            if dic[index][0] + value > dic[index][1]:
                answer += dic[index][0]
                temp = dic[index][1]
                while temp < dic[index][0] + value:
                    temp *= 2
                dic[index] = [dic[index][0] + value, temp]
            else:
                dic[index] = [dic[index][0]+value, dic[index][1]]
    return answer


a = [[1, 1], [1, 2], [1, 4], [1, 8]]
print(solution(a))
