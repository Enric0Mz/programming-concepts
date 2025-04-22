class TreeNode:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value: int):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node: TreeNode, value: int):
        if value < node.value:
            if node.left:
                self._insert_recursive(node.left, value)
            else:
                node.left = TreeNode(value)
        else:
            if node.right:
                self._insert_recursive(node.right, value)
            else:
                node.right = TreeNode(value)
        
            
    def search(self, value: int):
        return self._search_recursive(self.root, value)
    
    def _search_recursive(self, node: TreeNode, value: int):
        if not node:
            return False
        if node.value == value:
            return True
        if node.value < value:
            return self._search_recursive(node.right, value)
        return self._search_recursive(node.left, value)
    

tree = BinaryTree()
values_to_insert = [10, 5, 15, 3, 7, 12, 18]
for val in values_to_insert:
    tree.insert(val)

print(tree.search(7))
print(tree.search(14))
print(tree.search(10))
print(tree.search(18))

