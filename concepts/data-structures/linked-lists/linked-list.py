class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_front(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_to_end(self, value):
        new_node = Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def remove_from_front(self):
        if not self.head:
            return None
        removed_value = self.head.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return removed_value

    def remove_from_end(self):
        if not self.tail:
            return None
        removed_value = self.tail.value
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return removed_value
    

dll = DoublyLinkedList()

dll.add_to_front(10)
print("Lista após adicionar 10 no início:", dll.head.value)

dll.add_to_front(20)
print("Lista após adicionar 20 no início:", dll.head.value, dll.head.next.value)

dll.add_to_end(30)
print("Lista após adicionar 30 no final:", dll.head.value, dll.head.next.value, dll.tail.value)

removed = dll.remove_from_front()
print("Removido do início:", removed)
print("Lista após remoção do início:", dll.head.value if dll.head else "Lista vazia")

removed = dll.remove_from_end()
print("Removido do final:", removed)
print("Lista após remoção do final:", dll.head.value if dll.head else "Lista vazia")

