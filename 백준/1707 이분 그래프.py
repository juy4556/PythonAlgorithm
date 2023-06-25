import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline


def dfs(nodes, num, color):
    global flag
    colors[num] = color
    for node in nodes[num]:
        if colors[node] == 0:
            dfs(nodes, node, -color)
        elif colors[node] == color:
            flag = True
            return


if __name__ == "__main__":
    K = int(input())
    for k in range(K):
        v, e = map(int, input().split())
        nodes = [[] for _ in range(v + 1)]
        colors = [0 for _ in range(v + 1)]
        flag = False
        for i in range(e):
            a, b = map(int, input().split())
            nodes[a].append(b)
            nodes[b].append(a)
        for i in range(1, v + 1):
            if flag:
                break
            if colors[i] == 0:
                dfs(nodes, i, 1)
        if flag:
            print("NO")
            continue
        print("YES")
