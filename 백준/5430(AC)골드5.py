import sys
from collections import deque

t = int(input())  # 테스트 케이스 개수(최대 100)
for i in range(t):
    flag = 0
    p = input()  # 수행할 함수 p(1이상 100,000이하)
    n = int(input())  # 배열에 들어있는 수의 개수 n

    array = sys.stdin.readline().strip()[1:-1].split(",")
    q = deque(array)
    reverse_count = 0

    if n == 0:
        q = []
    for j in p:
        if j == 'R':
            reverse_count += 1
        elif j == 'D':
            if not q:
                flag = 1
                print("error")
                break
            else:
                if reverse_count % 2 == 0:
                    q.popleft()
                else:
                    q.pop()

    if flag == 0:
        if reverse_count % 2 == 1:
            q.reverse()
        print("[" + ",".join(q) + "]")
