class Node:
    def __init__(self,data):
        self.left = None
        self.right = None
        self.data = data
        self.count = 0

    def insert(self,data):
        if self.data:
            if data >self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
            if data<self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
        else:
            self.data = data

    def printTree(self):
        if self.left: 
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

    

root = Node(12)
root.insert(14)
root.insert(35)
root.insert(31)
root.insert(10)
root.insert(19)
root.printTree()

