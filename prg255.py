#2.19-06-2026 priorityqueue
import heapq
class PriorityQueue:
    def __init__(self):
        self.heap =[]
        self.counter = 0
    def insert(self, item,priority):
        heapq.heappush(self.heap, (priority,self.counter,item))
        self.counter += 1
        print(f"Inserted '{item}' with priority {priority}")
    def extractMin(self):
        if self.isEmpty(): return "Queue Empty!"
        priority, _, item = heapq.heappop(self.heap)
        print(f"Extracted '{item}' priority{priority}")
        return item
    def peek(self):
        return self.heap[0][2] if not self.isEmpty() else "Empty"
    def isEmpty(self):
        return len(self.heap) == 0
    def size(self):
        return len(self.heap)
pq=PriorityQueue()
pq.insert("Low Task",5)
pq.insert("High Task",1)
pq.insert("Med Task",3)
print("peek:",pq.peek())
pq.extractMin()
pq.extractMin()
