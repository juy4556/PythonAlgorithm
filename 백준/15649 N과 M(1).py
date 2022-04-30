N, M = map(int, input().split())
visited = [False] * (N + 1)
perm = []


def solution():
    if len(perm) == M:
        print(perm)
        return
    for i in range(1, N + 1):
        if not visited[i]:
            visited[i] = True
            perm.append(i)
            solution()
            perm.pop()
            visited[i] = False


solution()
