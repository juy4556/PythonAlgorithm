import sys
from collections import defaultdict

input = sys.stdin.readline
if __name__ == "__main__":
    T = int(input())
    for _ in range(T):
        W = input()
        K = int(input())
        _min, _max = 10001, 0
        flag = 0
        dic = defaultdict(list)
        for i in range(len(W)):
            dic[W[i]].append(i)

        for value in dic.values():
            if len(value) < K:
                continue
            flag = 1
            for i in range(len(value) - K + 1):
                length = value[i + K - 1] - value[i] + 1
                if _min > length:
                    _min = length
                if _max < length:
                    _max = length
        if flag:
            print(_min, _max)
        else:
            print(-1)
