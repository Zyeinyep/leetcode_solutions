# Adds two numbers represented as linked lists.
# Logic: Traverse both lists, add digits with carry, continue with the longer list, 
#        add a final node if carry remains.
# Time: O(max(m, n)), Space: O(max(m, n)) for the new list.

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        total = ListNode()
        carry = 0
        run = 0

        while l1 and l2:
            added = l1.val + l2.val + carry
            carry = added // 10
            added %= 10

            if run == 0:
                total.val = added
            elif run == 1:
                total.next = ListNode(added)
                last = total
            else:
                last = last.next
                last.next = ListNode(added)

            l1 = l1.next
            l2 = l2.next
            run += 1

        while l1 or l2:
            node = l1 if l1 else l2
            added = node.val + carry
            carry = added // 10
            added %= 10
            last = last.next
            last.next = ListNode(added)
            if l1: l1 = l1.next
            if l2: l2 = l2.next

        if carry:
            last = last.next
            last.next = ListNode(carry)

        return total
