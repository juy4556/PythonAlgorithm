def find_bingo(arr, bingo):
    for i in range(3):
        horse = arr[i]
        if horse == '.':
            continue
        x_bingo = 1
        for j in range(i, 9, 3):
            if arr[j] != horse:
                x_bingo = 0
                break
        if x_bingo:
            bingo[horse][0] += 1

    # 열빙고
    for i in range(0, 9, 3):
        horse = arr[i]
        if horse == '.':
            continue
        y_bingo = 1
        for j in range(i + 1, i + 3):
            if arr[j] != horse:
                y_bingo = 0
                break
        if y_bingo:
            bingo[horse][1] += 1

    # 대각선빙고
    if arr[0] != '.' and arr[0] == arr[4] and arr[0] == arr[8]:
        bingo[arr[0]][2] = 1
    if arr[2] != '.' and arr[2] == arr[4] and arr[2] == arr[6]:
        bingo[arr[2]][2] = 1

    return


if __name__ == "__main__":
    bingo = dict()

    while True:
        s = input()
        if s == "end":
            break
        bingo['X'] = [0, 0, 0]
        bingo['O'] = [0, 0, 0]
        o_count = s.count('O')
        x_count = s.count('X')
        if x_count == o_count or x_count == o_count + 1:
            pass
        else:
            print("invalid")
            continue

        find_bingo(s, bingo)
        x1, y1, z1 = bingo['X']
        x2, y2, z2 = bingo['O']
        x_bingo = bingo['X'].count(1)
        o_bingo = bingo['O'].count(1)
        if x1 > 1 or y1 > 1 or z1 > 1 or x2 > 1 or y2 > 1 or z2 > 1:
            print("invalid")
        elif x_bingo and o_bingo:
            print("invalid")
        elif x_bingo and x_count != o_count + 1:
            print("invalid")
        elif o_bingo and x_count != o_count:
            print("invalid")
        elif not x_bingo and not o_bingo and x_count + o_count < 9:
            print("invalid")
        else:
            print("valid")
