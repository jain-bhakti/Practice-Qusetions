class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Tree:
    def __init__(self,val):
        self.root = TreeNode(val)
    
    def BuildTree(self,val):
        if self.root

p = [1,2,3]
q = [1,2,3]

def isSameTree(self, p, q) :
    if not p and not q:
        return True

    if not q or not p:
        return False

    if p.val != q.val:
        return False

    return self.isSameTree(p.right, q.right) and self.isSameTree(p.left, q.left)

