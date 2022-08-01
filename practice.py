dir = {0: 'left', 1: 'right', 2: 'up', 3: 'down'}
def left():
    return 'hi'
for i in range(4):
    print(dir[i]())