# Adds two numbers represented as linked lists in reverse order.
# Logic:
# - Traverse both lists simultaneously and add corresponding digits with any carry.
# - Use a dummy head to simplify list construction.
# - If a list is shorter, treat missing digits as 0.
# - After processing both lists, if there is a remaining carry, add a final node.
# Runtime: O(max(m, n)) — each node is visited once.
# Space: O(max(m, n)) — for the output list; no extra data structures used.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummy = ListNode(0)  # dummy head for result list
        current = dummy
        carry = 0

        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            total = x + y + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            current.next = ListNode(carry)

        return dummy.next
