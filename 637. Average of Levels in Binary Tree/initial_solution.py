# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: List[float]
        
        Time Complexity: O(n)  # visit each node once
        Space Complexity: O(w) # max width of the tree stored in queue
        """
        avg = []
        queue = []
        queue.append(root)
        
        while len(queue) > 0:
            level_size = len(queue)
            level_sum = 0
          
            for i in range(level_size):
                curr = queue.pop(0)
                level_sum += curr.val
         
                if curr.left:
                    queue.append(curr.left)
                if curr.right:
                    queue.append(curr.right)
                    
            avg.append(float(level_sum)/level_size)
            
        return avg
