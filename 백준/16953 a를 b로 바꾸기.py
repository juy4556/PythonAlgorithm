if __name__ == "__main__":
    a, b = map(int, input().split())
    count = 1
    while b > a:
        count += 1
        if b % 2 == 0:  # 짝수 일 때
            b //= 2
        else:  # 홀수
            if b % 10 == 1:  # 끝 자리가 1이면 10으로 나눔
                b //= 10
            else:  # 끝자리가 홀수이고 1이 아니면 멈춤
                break

    if a == b:
        print(count)
    else:
        print(-1)
