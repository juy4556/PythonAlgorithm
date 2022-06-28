bitmap = [["3C", "42", "81", "81", "81", "81", "42", "3C"], ["08", "18", "08", "08", "08", "08", "08", "1C"],
          ["3C", "42", "81", "02", "1C", "20", "40", "FF"], ["7E", "81", "02", "1C", "02", "01", "81", "7E"],
          ["04", "0C", "14", "24", "44", "84", "FF", "04"], ["FF", "80", "80", "FC", "42", "01", "81", "7E"],
          ["7E", "80", "80", "80", "FE", "81", "81", "7E"], ["7F", "02", "04", "08", "10", "20", "40", "00"],
          ["7E", "81", "81", "7E", "81", "81", "81", "7E"], ["7E", "81", "81", "81", "FF", "01", "01", "7E"]]

word = "23"


def solution(word):
    length = len(word) // 16 + 1
    for i in range(length, 32):
        word + " "
    answer = ["0x"] * (len(word))
    for i in range(len(answer)):
        index = i // 8
        if word[i] == '0':
            for j in range(8):
                answer[index] += bitmap[0][j]
                index += 4
        elif word[i] == '1':
            for j in range(8):
                answer[index] += bitmap[1][j]
                index += 4
        elif word[i] == '2':
            for j in range(8):
                answer[index] += bitmap[2][j]
                index += 4
        elif word[i] == '3':
            for j in range(8):
                answer[index] += bitmap[3][j]
                index += 4
        elif word[i] == '4':
            for j in range(8):
                answer[index] += bitmap[4][j]
                index += 4
        elif word[i] == '5':
            for j in range(8):
                answer[index] += bitmap[5][j]
                index += 4
        elif word[i] == '6':
            for j in range(8):
                answer[index] += bitmap[6][j]
                index += 4
        elif word[i] == '7':
            for j in range(8):
                answer[index] += bitmap[7][j]
                index += 4
        elif word[i] == '8':
            for j in range(8):
                answer[index] += bitmap[8][j]
                index += 4
        elif word[i] == '9':
            for j in range(8):
                answer[index] += bitmap[9][j]
                index += 4
        elif word[i] == ' ':
            print(answer)
            for j in range(8):
                answer[index] += "0"
                index += 4
        else:
            continue

    for i in range(len(answer)-1):
        for j in range(4):
            print(answer[4 * i + j], end=" ")
        print()


solution(word)
