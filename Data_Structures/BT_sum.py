class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def addBT(root):
    if root == None:
        return 0
    return (root.val + addBT(root.left) + addBT(root.right))

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
print(addBT(root))