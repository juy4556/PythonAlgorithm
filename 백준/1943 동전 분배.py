if __name__ == "__main__":
    for _ in range(3):
        N = int(input())
        coins = {}
        key_set = []
        for _ in range(N):
            price, count = map(int, input().split())
            coins[price] = count
            key_set.append(price)

        key_set.sort(reversed)
        a, b = 0, 0
        for k in key_set:
            if coins[k] % 2 == 0:
                continue
            if a < b:
                a += k * coins[k]
            else:
                b += k * coins[k]

            if a == b:
                a = 0
                b = 0

        '''
        50 40 30 10 
        '''
