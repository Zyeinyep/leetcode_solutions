"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
import copy
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
       # Time and Space complexity: O(n)
        if not head:
            return None
        mapped = {}
        curr = head
        while curr:
            mapped[curr] = Node(curr.val, None)
            curr = curr.next
        curr = head
        
        while curr:
            m = mapped[curr]
            m.next = mapped.get(curr.next)
            m.random = mapped.get(curr.random)
            curr = curr.next

        return mapped[head]

        
        
