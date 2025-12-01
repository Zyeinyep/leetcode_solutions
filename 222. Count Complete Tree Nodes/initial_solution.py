# Time Complexity: O(n) — we visit every node once in the DFS traversal.
# Space Complexity: O(n) — worst case stack size for an unbalanced tree.

class Solution(object):
    def countNodes(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        stack = []
        count = 0
       
        if root:
            stack.append(root)
    
        while len(stack) > 0:
            curr = stack.pop()
            
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
            
            count += 1
        
        return count
