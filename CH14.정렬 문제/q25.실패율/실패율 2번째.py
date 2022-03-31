import sys
input = sys.stdin.readline

N = int(input())
stages = list(map(int, input().split()))

def solution(N, stages):
    answer = []
    stages.sort()
    num = len(stages)
    for i in range(1, N+1):
        cnt = stages.count(i)
        if num == 0:
            fail_rate = cnt
        else:
            fail_rate = cnt/num
        answer.append((i, fail_rate))
        num -= cnt
    answer.sort(key = lambda x:x[1], reverse=True)
    answer = [i[0] for i in answer]
    return answer

print(solution(N, stages))

