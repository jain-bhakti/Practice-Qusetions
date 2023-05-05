class BinaryTreeNode:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self,data):
        if data==self.data:
            return

        if data < self.data:
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinaryTreeNode(data)
        else:
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinaryTreeNode(data)

    def PrintTree(self):
        elements = []
        if self.left:
            elements += self.left.PrintTree()

        elements.append(self.data)

        if self.right:
            elements += self.right.PrintTree()
        return elements


def build_tree(elements):
    root = BinaryTreeNode(elements[0])
    for i in range(1,len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
     numbers_tree = build_tree([17, 4, 1, 20, 9, 23, 18, 34])
     print("In order traversal gives this sorted list:",numbers_tree.PrintTree())