R, C, M = map(int, input().split())
sharks = []
result = 0
for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks.append([r, c, s, d, z])


def capture_shark(c):
    global sharks, result
    idx = 0
    flag = False
    for n in range(len(sharks)):
        if sharks[n][1] == c:
            flag = True
            result += sharks[n][4]
            idx = n
            break
    if flag:
        sharks = sharks[:idx] + sharks[idx + 1:]


def move_shark():
    global sharks
    for n in range(len(sharks)):
        x, y, speed, dir = sharks[n][0], sharks[n][1], sharks[n][2], sharks[n][3]
        new_x, new_y, new_d = x, y, dir
        if dir == 1:  # 위
            temp = speed % (2 * R - 2)
            if (R-x-1 - temp // R) % 2:  # 홀
                new_d = (dir + 2) % 4
                new_x = R - (x + temp) % R
            else:
                new_x = (x + temp) % (R - 2)
        elif dir == 2:  # 아래
            temp = speed % (2 * R - 2)
            if (x + temp // R) % 2:  # 홀
                new_d = (dir + 2) % 4
                new_x = R - (x+temp) % R
            else:
                new_x = (x+temp) %
        elif dir == 3:  # 오른
            new_y = (y + speed) % (2 * C - 2) + 1
            if (y + speed // C - 1) % 2 == 1:
                new_d = (dir + 2) % 4

        elif dir == 4:  # 왼
            new_y = (y - speed) % (2 * C - 2) + 1
            if (y - speed // C - 1) % 2 == 1:
                new_d = (dir + 2) % 4
        sharks[n][0], sharks[n][1], sharks[n][3] = new_x, new_y, new_d
    # 같은 위치 상어 중 가장 큰 상어만 남기기
    sharks.sort(key=lambda s: (s[0], s[1], -s[4]))  # x,y 작은 순, 사이즈는 큰 순 정렬
    a, b = sharks[0][0], sharks[0][1]
    new_sharks = []
    new_sharks.append(sharks[0])
    for n in range(1, len(sharks)):
        if a == sharks[n][0] and b == sharks[n][1]:
            continue
        else:
            a, b = sharks[n][0], sharks[n][1]
            new_sharks.append(sharks[n])
    sharks = new_sharks


def solution():
    sharks.sort(key=lambda x: (x[0], x[1]))
    for c in range(1,C+1):  # 열
        capture_shark(c)
        print(sharks)
        move_shark()
    print(result)


solution()