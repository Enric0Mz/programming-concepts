class Node:
    def __init__(self, value: int) -> None:
        self.value = value
        self.next = None
        self.prev = None


class Queue:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self) -> int:
        return self.size


    def append(self, value: Node) -> None:
        new_value = Node(value)
        if not self.head:
            self.head = new_value
            self.tail = new_value
        else:
            new_value.prev = self.tail
            self.tail.next = new_value
            self.tail = new_value
        self.size += 1
    
    def popleft(self) -> int:
        if not self.head:
            raise IndexError("Cannot pop left from empty list")
        
        popped_item = self.head
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        else:
            self.head.prev = None
        self.size -= 1
        return popped_item.value

    def peek(self) -> int:
        if not self.head:
            raise IndexError("Cannot peek from empty list")

        return self.head.value



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