from collections import deque

queue = deque()

queue.append(5)
queue.append(4)
queue.append(3)
queue.popleft() # first out
queue.append(2)
queue.append(1)
queue.pop() # last out
queue.appendleft(7) # last append to the first
print(queue)
queue.reverse()
print(queue)