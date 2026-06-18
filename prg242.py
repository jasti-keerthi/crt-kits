class CircularQueue:
    def __init__(self,size):
        self.size=size
        self.queue=[None]*size
        self.front=-1
        self.rear=-1
    def IsFull(self):
        return(self.rear+1)% self.size==self.front
    def isEmpty(self):
       return self.front==-1
    def enqueue(self, value):
        if(self.IsFull()):
            return "Queue Over Flow!"
        if self.isEmpty():self.front=0
        self.rear=(self.rear+1)%self.size
        self.queue[self.rear+1]=value
        print(f"Enqueued {value} at index {self.rear}")
    def dequeue(self):
        if self.isEmpty():
            return "Queue Underflow!"
        val=self.queue[self.front]
        self.queue[self.front]=None
        if self.front==self.rear:
            self.front=self.rear=-1
        else:
            self.front=(self.front+1)%self.size
        return val
    def display(self):
        if self.isEmpty():print("Empty");return
        i,elems= self.front,[]
        while True:
            elems.append(self.queue[i])
            if i==self.rear:break
            i=(i+1)%self.size
        print("CQ:",elems)
d=CircularQueue(5)
d.enqueue(10)
d.enqueue(20)
d.enqueue(30)
print(d.display())
print(d.isEmpty())
d.dequeue()
print(d.display())