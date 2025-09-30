from typing import List
from collections import deque

class TreeNode:
    def __init__(self, value: int) -> None:
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, value: int) -> None:
        node = TreeNode(value)
        if not self.root:
            self.root = node
        else:
            self._insert_recursive(self.root, node)

    def _insert_recursive(self, node: TreeNode, new_node: TreeNode) -> None:
        if new_node.value > node.value:
            if not node.right:
                node.right = new_node
            else:
                self._insert_recursive(node.right, new_node)
        else:
            if not node.left:
                node.left = new_node
            else:
                self._insert_recursive(node.left, new_node)

    def search(self, value: int) -> bool:
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: TreeNode, value: int) -> bool:
        if not node:
            return False
        if node.value == value:
            return True
        elif value > node.value:
            return self._search_recursive(node.right, value)
        else:
            return self._search_recursive(node.left, value)
    
    # DFS        
    def pre_order_traversal(self) -> List:
        result = []
        self._pre_order_traversal(self.root, result)
        return result

    def _pre_order_traversal(self, node: TreeNode, result: List) -> List:
        if node:
            result.append(node.value)
            self._pre_order_traversal(node.left, result)
            self._pre_order_traversal(node.right, result)
    # DFS
    def in_order_traversal(self) -> List:
        result = []
        self._in_order_traversal(self.root, result)
        return result

    def _in_order_traversal(self, node: TreeNode, result: List) -> List:
        if node:
            self._in_order_traversal(node.left, result)
            result.append(node.value)
            self._in_order_traversal(node.right, result)
    # DFS
    def post_order_traversal(self) -> List:
        result = []
        self._post_order_traversal(self.root, result)
        return result
    
    def _post_order_traversal(self, node: TreeNode, result: List) -> List:
        if node:
            self._post_order_traversal(node.left, result)
            self._post_order_traversal(node.right, result)
            result.append(node.value)

    # DFS
    def pre_order_traversal_iterative(self):
        stack = [self.root]
        result = []

        while stack:
            node = stack.pop()
            result.append(node.value)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return result
    
    # BFS
    def level_order_traversal(self):
        q = deque()
        q.append(self.root)

        result = []

        while q:
            node = q.popleft()
            result.append(node.value)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        
        return result

    
tree = BinaryTree()

nums = [5,4,7,2,6,9]

for num in nums: 
    tree.insert(num)

print(tree.root.value)

print("Procurando 4... ", tree.search(4)) # True
print("Procurando 9... ", tree.search(9)) # True
print("Procurando 1... ", tree.search(1)) # False

print("Items da lista... (Pre Order)", tree.pre_order_traversal()) # [5,4,2,7,6,9]
print("Items da lista... (In Order)", tree.in_order_traversal()) # [2,4,5,6,7,9]
print("Items da lista... (Post Order)", tree.post_order_traversal()) # [2,4,6,9,7,5]

print("Items da lista... (Pre Order Iterativa)", tree.pre_order_traversal_iterative()) # [5,4,2,7,6,9]
print("Items da lista... (Level Order (BFS))", tree.level_order_traversal()) # [5,4,7,2,6,9]
