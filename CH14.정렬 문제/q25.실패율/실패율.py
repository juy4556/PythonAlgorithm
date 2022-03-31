import sys
input = sys.stdin.readline
n = int(input())
stage = list(map(int, input().split()))


def solution(N, stages):
    answer = []

    length = len(stages)
    for i in range(1, N+1):
        count = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = count/length

        answer.append((fail, i))
        length -= count

    answer.sort(key=lambda x: x[0], reverse=True)
    answer = [i[1] for i in answer]
    return answer


print(solution(n, stage))