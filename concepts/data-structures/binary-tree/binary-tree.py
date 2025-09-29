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


    
tree = BinaryTree()

nums = [5,4,7,2,6,9]

for num in nums:
    tree.insert(num)

print(tree.root.value)

print("Procurando 4... ", tree.search(4)) # True
print("Procurando 9... ", tree.search(9)) # True
print("Procurando 1... ", tree.search(1)) # False  
