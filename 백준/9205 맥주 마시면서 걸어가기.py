from collections import deque


def bfs(points):
    q = deque()
    q.append(points[0])
    visited = [0 for _ in range(len(points))]
    visited[0] = 1
    while q:
        x, y = q.popleft()
        if [x, y] == points[-1]:
            return 1
        for i in range(1, len(points)):
            if not visited[i] and abs(x - points[i][0]) + abs(y - points[i][1]) <= 1000:
                q.append(points[i])
                visited[i] = 1
    return 0


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        points = [list(map(int, input().split()))]
        for _ in range(n):
            points.append(list(map(int, input().split())))
        points.append(list(map(int, input().split())))

        if bfs(points):
            print("happy")
            continue
        print("sad")
