a = [[0 for _ in range(5)]for _ in range(5)]
print(a)
for i in range(5):
    a[i] = a[i][:1]+a[i][2:]
print(a)
for i in range(5):
    for _ in range(3):
        a[i] = [0] + a[i]
print(a)