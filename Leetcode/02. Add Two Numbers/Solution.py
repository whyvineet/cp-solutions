# https://leetcode.com/problems/add-two-numbers/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def solve(l1, l2, carry):

            if not l1 and not l2 and not carry:
                return None

            a = l1.val if l1 else 0
            b = l2.val if l2 else 0

            sm = a + b + carry
            node = ListNode(sm%10)

            node.next = solve(l1.next if l1 else None, l2.next if l2 else None, sm//10)

            return node

        return solve(l1, l2, 0)