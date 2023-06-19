from collections import deque

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
if __name__ == "__main__":
    count = 0
    while True:
        N = int(input())
        if N == 0:
            break
        count += 1
        space = []
        array = [[int(1e9) for _ in range(N)] for _ in range(N)]
        for _ in range(N):
            space.append(list(map(int, input().split())))

        q = deque([[0, 0]])
        array[0][0] = space[0][0]
        while q:
            x, y = q.popleft()
            for d in range(4):
                nx = x + dx[d]
                ny = y + dy[d]
                if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                    continue
                if array[x][y] + space[nx][ny] < array[nx][ny]:
                    array[nx][ny] = array[x][y] + space[nx][ny]
                    q.append([nx, ny])

        print('Problem {0}: {1}'.format(count, array[N-1][N-1]))
