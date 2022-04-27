import sys
import math
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    x, y = map(int, input().split())
    n = int(math.sqrt(y-x))
    nn = int(math.sqrt(y-x+n))
    if pow(nn,2)-nn+1 <= y-x <= pow(nn, 2):
        print(2*nn-1)
    elif pow(nn,2) < y-x <=nn*(nn+1):
        print(2*nn)