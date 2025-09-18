class Queue:
    def __init__(self):
        self.items = []

    def __len__(self):
        return len(self.items)
    
    def append(self, value):
        self.items.append(value)

    def popleft(self):
        if not len(self.items):
            raise IndexError("Cannot pop from empty queue")
        self.items.pop(0)

    def peek(self):
        if not len(self.items):
            raise IndexError("Cannot peek from empty queue")
        return self.items[0]

queue = Queue()

queue.append(1)

print("First Item", queue.peek())

queue.append(3)
print("First Item", queue.peek())

queue.append(5)
print("First Item", queue.peek())

queue.append(7)
print("First Item", queue.peek())

print("Size", len(queue))
print("Popped Item", queue.popleft())
print("New First Item in Queue", queue.peek())
print("New Size", len(queue))
