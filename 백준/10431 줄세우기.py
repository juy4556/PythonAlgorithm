if __name__ == "__main__":
    P = int(input())
    for tc in range(P):
        arr = list(map(int, input().split()))
        line = [arr[1]]
        steps = 0
        for i in range(2, 21):
            if line[-1] < arr[i]:
                line.append(arr[i])
                continue
            for j in range(len(line)):
                if line[j] > arr[i]:
                    steps += i - 1 - j
                    line.insert(j, arr[i])
                    break
        print(tc + 1, steps)
