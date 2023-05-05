class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def preorderTraversal(self, root):
        answer = []
        
        def dfs(node):
            if not node:
                return
            # Visit root first, then the left subtree, then the right subtree.
            answer.append(node.val)
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return answer

    def preorderTraversal_itr(self, root):
        answer = []
        stack = []
        stack.append(root)
        while stack:
            currnode = stack.pop()
            if currnode:
                answer.append(currnode.val)
                stack.append(currnode.left)
                stack.append(currnode.right)

        return answer

    