def isSymmetric(root):
    if root is None:
        return True

    def mirror(node1,node2):
        if node1 is None and node2 is None:
            return True

        if node1 is None or node2 is None:
            return False
            
        if node1.val != node2.val:
            return False

        return (mirror(node1.left,node2.right) and mirror(node1.right,node2.left))

    return mirror(root.left,root.right)

root = [1,2,2,3,4,4,3]