# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: Optional[TreeNode]
        :type q: Optional[TreeNode]
        :rtype: bool
        """
        # Time and Space comp: O(n)

        arr = [p]
        arr2 = [q]
        if q == None and p == None:
            return True

        
        
        while len(arr) != 0 and len(arr2) != 0:
           
            curr = arr.pop()
            curr2 = arr2.pop()
           
            
            if curr is None or curr2 is None:
                return False

            if curr.val != curr2.val:
                return False
            if (curr.left is None) != (curr2.left is None):
                return False
            if (curr.right is None) != (curr2.right is None):
                return False
            

            if curr.right != None and curr2.right != None:
                arr.append(curr.right)
                arr2.append(curr2.right)
                if curr.left != None and curr2.left != None:
                    arr.append(curr.left)
                    arr2.append(curr2.left)
                
            elif curr.left != None and curr2.left!= None:
                arr.append(curr.left)
                arr2.append(curr2.left)
                if curr.right != None and curr2.right != None:
                    arr.append(curr.right)
                    arr2.append(curr2.right)
              
            elif curr.left == None and curr.right == None and curr2.left == None and curr2.right == None:
                continue
            else:
                return False
        return True


        
