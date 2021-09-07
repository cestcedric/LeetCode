# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return None

        # O(n) time
        # O(n) space: call stack with depth n
        def reverseRec(prev: ListNode, curr: ListNode) -> ListNode:
            if curr is None: return prev
            next = curr.next
            curr.next = prev
            return reverseRec(curr, next)

        # O(n) time
        # O(1) space: only three temporary extra variables needed
        def reverseIt(node: ListNode) -> ListNode:
            prev, curr = None, node

            while curr is not None:
                succ = curr.next
                curr.next = prev
                prev = curr
                curr = succ

            return prev

        return reverseIt(None, head)



        
        
        