n = 1270
count=0

#큰 단위화폐부터 확인
list=[500, 100, 50 ,10]

for coin in list:
    count += n // coin
    n %= coin

print(count)