def postorderTraversal(self, root):
        # Return an empty list if the root is None
        if not root:
            return []
        
        # Initialize an empty list to store the traversal and a stack to store the nodes
        ans = []
        stack = [root]
        
        # Iterate until the stack is empty
        while stack:
            # Pop the top node from the stack
            curr = stack.pop()
            # Append the node's value to the list
            ans.append(curr.val)
            # Push the left child of the node onto the stack (if it exists)
            if curr.left:
                stack.append(curr.left)
            # Push the right child of the node onto the stack (if it exists)
            if curr.right:
                stack.append(curr.right)
        
        # Reverse the list to convert the preorder traversal to a postorder traversal
        ans = ans[::-1]
        # Return the list of traversed values
        return ans