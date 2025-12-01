# Time Complexity: O((log n)^2)
# Space Complexity: O(1)

class Solution(object):
    def countNodes(self, root):
        if not root:
            return 0
        
        # function to compute the height of leftmost path
        def left_height(node):
            h = 0
            while node:
                node = node.left
                h += 1
            return h
        
        # function to compute the height of rightmost path
        def right_height(node):
            h = 0
            while node:
                node = node.right
                h += 1
            return h
        
        lh = left_height(root)
        rh = right_height(root)
        
        # If left height == right height → perfect tree
        if lh == rh:
            return (1 << lh) - 1    # 2^lh - 1
        
        # Otherwise count recursively
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)
