from collections import deque

cola = deque([1,2,3,4,5])
cola.append(6)
cola.appendleft(0)
print(cola)
cola.pop()
cola.popleft()
print(cola)
