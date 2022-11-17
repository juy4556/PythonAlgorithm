def move(n, bridges):
    people = [[i,0] for i in range(1, n+1)] ## 행, 열 번호
    for i in range(1, n+1):
        for j in range(len(bridges)):
            if bridges[j][0] == array[i]:



if __name__ == "__main__":
    n, m = map(int, input().split())
    bridges = []
    for _ in range(m):
        a, b = map(int, input().split())
        bridges.append((a, b))

    move(n, bridges)
