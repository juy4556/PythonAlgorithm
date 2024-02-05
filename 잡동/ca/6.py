dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]
dir = ['d', 'l', 'r', 'u']


def move(now, end, answer, n, m):
    if end[0] - now[0] > 0:  # down
        if now[0] + 1 <= n:
            now[0] += 1
            answer.append('d')

    elif end[1] - now[1] < 0:  # left
        if now[1] - 1 >= 1:
            now[1] -= 1
            answer.append('l')

    elif end[1] - now[1] > 0:  # right
        if now[1] + 1 <= m:
            now[1] += 1
            answer.append('r')

    elif end[0] - now[0] < 0:  # up
        if now[0] - 1 >= 1:
            now[0] -= 1
            answer.append('u')


def solution(n, m, x, y, r, c, k):
    answer = []
    now = [x, y]
    end = [r, c]
    first = [x, y]
    front,back = [], []
    for _ in range(k):
        if now == end:
            for d in range(4):
                nx = now[0] + dx[d]
                ny = now[1] + dy[d]
                if 1 <= nx <= n and 1 <= ny <= m:
                    now = [nx, ny]
                    if ord(answer[0]) >= ord(dir[d]):
                        fx = first[0] + dx[d]
                        fy = first[1] + dy[d]
                        if 2 <= fx <= n-1 and 2 <= fy <= m-1:
                            first = [fx, fy]
                            front.append(dir[d])
                    else:
                        back.append(dir[d])
                    break
        else:
            move(now, end, answer, n, m)

    if now != end:
        return "impossible"
    front = ''.join(front)
    back = ''.join(back)
    answer = front+''.join(answer)+back
    return answer
