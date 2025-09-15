class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
        self.size = 0

    def __len__(self):
        return self.size

    def push(self, item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
        self.size += 1


    def pop(self):
        if not self.head:
            raise IndexError("Cannot pop from an empty stack")
        
        popped_item = self.head
        self.head = popped_item.next
        popped_item.next = None
        self.size -= 1
        return popped_item.value
    
    def peek(self):
        if not self.head:
            raise IndexError("Cannot peek from an empty stack")

        return self.head.value
    

stack = Stack()

stack.push(1)
stack.push(3)
stack.push(5)
stack.push(7)

print("Tamanho Inicial", len(stack))
print("Último Item", stack.peek())
print("Item removido",stack.pop())
print("Novo Último Item", stack.peek())
print("Tamanho Final", len(stack))
print(stack.pop())
print(stack.pop())
print(stack.pop())
print(stack.peek()) # Deve lançar IndexError
