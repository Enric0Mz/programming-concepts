class Stack:
    def __init__(self, max_lenght=1000):
        self.items = [0] * max_lenght
        self.max_lenght = max_lenght
        self.pointer = 0

    def __len__(self):
        return self.pointer

    def push(self, item):
        if self.pointer >= self.max_lenght:
            raise IndexError("Stack overflow")
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if self.pointer == 0:
            raise IndexError("The stack is empty")
        self.pointer -= 1
        popped_item = self.items[self.pointer]
        self.items[self.pointer] = 0
        return popped_item

    def peek(self):
        if self.pointer == 0:
            raise IndexError("The stack is empty")

        return self.items[self.pointer - 1]



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