N, K = map(int, input().split())
electrical_appliances = list(map(int, input().split()))
q = []
result = 0
for i in range(K):
    if electrical_appliances[i] in q:
        continue
    if len(q) < N:
        q.append(electrical_appliances[i])
        continue
    # 멀티탭에 구멍이 없으면서 새로운 전자제품 꽂아야 할 때
    next_uses = []
    for j in range(N):
        if q[j] in electrical_appliances[i:]:
            next_use = electrical_appliances[i:].index(q[j]) # 멀티탭에 꽂아 있는 제품을 다음에 언제 사용하는지
        else:
            next_use = 101
        next_uses.append(next_use)
    out = next_uses.index(max(next_uses)) # 가장 늦게 사용하는 제품 뽑기
    q.pop(out)
    q.append(electrical_appliances[i])
    result += 1

print(result)