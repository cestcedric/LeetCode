# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) time, O(1) space
    @staticmethod
    def linkedListLength(head: ListNode) -> int:
        l = 0
        while head != None:
            l += 1
            head = head.next
        return l


    # O(1) time, O(1) space
    @staticmethod
    def getSteps(length: int, steps: int) -> tuple:
        stepsize = length // steps
        if stepsize * steps == length: return (stepsize, steps, 0, 0)

        missing = length - stepsize * steps
        return (stepsize + 1, missing, stepsize, steps - missing)


    # O(k) time, O(1) space
    @staticmethod
    def getFirstK(head: ListNode, k: int) -> tuple:
        if k == 0: return None, head

        tmp = head
        for _ in range(k - 1):
            if tmp is None: return head, None
            tmp = tmp.next

        suffix = tmp.next
        tmp.next = None
        return head, suffix


    # O(n + k) time: if k >> n, we create loads of empty lists at the end
    # O(1) space: if we count output space, then O(k)
    def splitListToParts(self, head: ListNode, k: int) -> list:
        if k == 1: return [head]

        length = Solution().linkedListLength(head)
        bigK, bigCount, smallK, smallCount = Solution().getSteps(length, k)

        splitList = []

        for _ in range(bigCount):
            part, head = Solution().getFirstK(head, bigK)
            splitList.append(part)

        for _ in range(smallCount):
            part, head = Solution().getFirstK(head, smallK)
            splitList.append(part)

        return splitList





        