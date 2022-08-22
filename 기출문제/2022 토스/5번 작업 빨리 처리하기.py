tasks = list(map(int, input().split()))

def solution(tasks):
    a = list(set(tasks))
    for i in range(len(a)):
        if tasks.count(a[i]) % 3 == 1:
            return -1
    return len(a)


print(solution(tasks))