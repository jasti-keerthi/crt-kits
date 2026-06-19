#1.19-06-2026
from collections import deque
class Deque:
    def __init__(self):
        self.dq = deque()
    def addFront(self,value):
        self.dq.appendleft(value)
        print(f"AddFront {value} -> {list(self.dq)}")
    def addRare(self, value):
        self.dq.append(value)
        print(f"AddRear {value} -> {list(self.dq)}")
    def removeFront(self):
        if self.isEmpty(): return "Empty!"
        val = self.dq.popleft()
        print(f"RemFront {val} -> {list(self.dq)}")
        return val
    def removeRare(self):
        if self.isEmpty(): return "Empty!"
        val = self.dq.pop()
        print(f"RemRare {val} -> {list(self.dq)}")
        return val
    def peekFront(self):
        return self.dq[0] if not self.isEmpty() else "Empty"
    def peekRare(self):
        return self.dq[-1] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return len(self.dq) == 0
dq = Deque()

dq.addFront(10)
dq.addRare(20)
dq.addFront(5)
dq.addRare(30)

dq.removeFront()
dq.removeRare()

print("Front:", dq.peekFront())
print("Rear:", dq.peekRare())
print("Empty?", dq.isEmpty())
