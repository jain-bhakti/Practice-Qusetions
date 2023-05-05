class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None

class Binary_tree:
    def __init__(self,root):
        self.root = Node(root)

    def preorder_print(self,start,traversal):
        if start:
            traversal += (str(start.value) + "-")
            traversal = self.preorder_print(start.left,traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal

    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "-")
            traversal = self.inorder_print(start.right, traversal)
        return traversal

    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "-")
        return traversal

    def levelorder_print(self, start):
        if start is None:
            return 

        queue = []
        queue.append(start)

        traversal = ""
        while len(queue) > 0:
            traversal += str(queue[-1].value)+ "-"
            node = queue.pop()

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return traversal


tree = Binary_tree(1)
tree.root.left = Node(2)
tree.root.right = Node(3)
tree.root.left.left = Node(4)
tree.root.left.right = Node(5)
tree.root.right.left = Node(6)
tree.root.right.right = Node(7)
print(tree.preorder_print(tree.root,""))
print(tree.inorder_print(tree.root,""))
print(tree.postorder_print(tree.root,""))


tree2 = Binary_tree(1)
tree2.root.left = Node(2)
tree2.root.right = Node(3)
tree2.root.left.left = Node(4)
tree2.root.left.right = Node(5)
print(tree2.levelorder_print(tree2.root))

