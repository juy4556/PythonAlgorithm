N = int(input())
green = [[0 for _ in range(4)] for _ in range(6)]  # block이 위치한 곳은 1, 없으면 0
blue = [[0 for _ in range(6)] for _ in range(4)]
score = 0


def plus_block(t, x, y):
    if t == 1:  # block이 1X1
        flag1, flag2 = False, False
        idx1, idx2 = 5, 5
        for i in range(6):
            if not flag1 and green[i][y] == 1:
                idx1 = i - 1
                flag1 = True
            if not flag2 and blue[x][i] == 1:
                idx2 = i - 1
                flag2 = True
        green[idx1][y] = 1
        blue[x][idx2] = 1
    elif t == 2:  # block이 1X2
        flag1, flag2 = False, False
        idx1, idx2 = 5, 5
        for i in range(6):
            if not flag1 and (green[i][y] == 1 or green[i][y + 1] == 1):
                idx1 = i - 1
                flag1 = True
            if not flag2 and blue[x][i] == 1:
                idx2 = i - 1
                flag2 = True
        green[idx1][y], green[idx1][y + 1] = 1, 1
        blue[x][idx2 - 1], blue[x][idx2] = 1, 1
    elif t == 3:  # block이 2X1
        flag1, flag2 = False, False
        idx1, idx2 = 5, 5
        for i in range(6):
            if not flag1 and green[i][y] == 1:
                idx1 = i - 1
                flag1 = True
            if not flag2 and (blue[x][i] == 1 or blue[x + 1][i] == 1):
                idx2 = i - 1
                flag2 = True
        green[idx1 - 1][y], green[idx1][y] = 1, 1
        blue[x][idx2], blue[x + 1][idx2] = 1, 1


def get_score():
    global score, green, blue
    cnt1, cnt2, cnt3 = 0, 0, 0
    for i in range(5, -1, -1):
        if 0 not in green[i]:
            score += 1
            green = green[:i] + green[i + 1:]
            cnt1 += 1
        cnt2 = 0
        for j in range(4):
            if blue[j][i] == 1:
                cnt2 += 1
        if cnt2 == 4:
            score += 1
            cnt3 += 1
            for k in range(4):
                blue[k] = blue[k][:i] + blue[k][i + 1:]

    for _ in range(cnt1):
        green = [[0, 0, 0, 0]] + green
    for i in range(4):
        for _ in range(cnt3):
            blue[i] = [0] + blue[i]


def check():
    global green, blue
    cnt1, cnt2 = 0, 0
    for i in range(2):
        if 1 in green[i]:
            cnt1 += 1
    for _ in range(cnt1):
        green = [[0, 0, 0, 0]] + green[:5]

    for i in range(2):
        for j in range(4):
            if blue[j][i] == 1:
                cnt2 += 1
                break

    for i in range(4):
        for _ in range(cnt2):
            blue[i] = [0] + blue[i][:5]


def get_result():
    print(score)
    blocks = 0
    for i in range(6):
        for j in range(4):
            if green[i][j] == 1:
                blocks += 1
            if blue[j][i] == 1:
                blocks += 1
    print(blocks)


def solution():
    for _ in range(N):
        t, x, y = map(int, input().split())
        plus_block(t, x, y)
        get_score()
        check()
    get_result()


solution()
