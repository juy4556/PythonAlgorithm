a = 1
b = []


def func1(a):
    a += 1


def func2(b):
    b.append(1)


func1(a)
func2(b)

print(a)
print(b)



