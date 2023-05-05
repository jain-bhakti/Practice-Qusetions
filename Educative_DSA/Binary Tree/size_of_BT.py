class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
    
class BinaryTree:
    def __init__(self,root):
        self.root = Node(root)

    def size_rec(self,node):
        if node is None:
            return 0
        return 1 + self.size_rec(node.left) + self.size_rec(node.right)


    def size_itr(self,node):
        if self.root is None:
            return 0

        stack = []
        stack.append(self.root)
        size = 1
        while stack:
            node = stack.pop()
            if node.left:
                size += 1
                stack.append(node.left)
            if node.right:
                size += 1
                stack.append(node.right)
        return size

tree2 = BinaryTree(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)
print(tree2.size_itr(tree2.root))
print(tree2.size_rec(tree2.root))
