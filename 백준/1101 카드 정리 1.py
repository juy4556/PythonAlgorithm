'''
1. 박스 최대 1개는 조커 박스로 지정할 수 있다. 조커 박스는 색이 다른 카드를 보관해도 된다.
2. 조커 박스를 제외한 모든 박스는 비어있거나, 같은 색의 카드만 보관해야 한다.
3. 같은 색을 가진 모든 카드는 모두 같은 박스에 있어야 한다.
    이때 조커 박스에 들어있는 카드는 제외한다.
    같은 색을 가진 모든 카드가 조커 박스에 들어있는 것도 가능하다.
'''
if __name__ == "__main__":
    N, M = map(int, input().split())  # N은 박스, M은 색상 수
    boxes = []
    result = N - 1
    for _ in range(N):
        cards = list(map(int, input().split()))
        boxes.append(cards)

    for n in range(N):
        count = 0
        color = [0] * M
        for i in range(N):
            if i == n:
                continue
            dif_count = 0
            idx = 0
            for j in range(M):
                if boxes[i][j]:
                    dif_count += 1
                    idx = j
            if dif_count > 1:
                count += 1
            elif dif_count == 1:
                if color[idx]:
                    count += 1
                else:
                    color[idx] = 1

        result = min(result, count)

    print(result)
