from collections import defaultdict
import sys

input = sys.stdin.readline
if __name__ == "__main__":
    G = int(input())
    P = int(input())
    g = []
    docked = [0 for _ in range(G)]
    log = defaultdict(int)
    for _ in range(P):
        g.append(int(input()))

    for i in range(P):
        index = g[i] - 1
        if log[index]:
            index = log[index]
        while index > 0 and docked[index]:
            index -= 1
        if not docked[index] and index <= g[i] - 1:
            docked[index] = 1
            log[g[i] - 1] = index
        else:
            break

    print(docked.count(1))
