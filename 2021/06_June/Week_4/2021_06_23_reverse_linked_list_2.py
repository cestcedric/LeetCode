# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) time complexity: passing through reversed part twice, but still linear
    # O(1) space complexity: no extra nodes created
    def reverseBetween2Pass(self, head: ListNode, left: int, right: int) -> ListNode:
        # generic reverse
        def reverse(head):
            prev, curr = None, head
            while curr is not None:
                curr.next, curr, prev = prev, curr.next, curr
            return prev, head

        firstNode, lastNode = head, head
        left_i, right_i = left, right
        prev, next = None, lastNode.next
        # find start of part to reverse
        while left_i > 1:
            prev = firstNode
            firstNode = firstNode.next
            lastNode = lastNode.next
            next = lastNode.next
            left_i -= 1
            right_i -= 1
        # end of part to reverse
        while right_i > 1:
            lastNode = lastNode.next
            next = lastNode.next
            right_i -= 1

        # detach list to be reversed
        lastNode.next = None

        # stitch list back together
        reversed = reverse(firstNode)
        if left > 1: 
            prev.next = reversed[0]
        else: 
            head = reversed[0]
        reversed[1].next = next

        return head


    # O(n) time complexity: one pass through list
    # O(1) space complexity: no extra nodes created
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        if left == right: return head
        prev, curr = None, head

        # find start of part to reverse
        while left > 1:
            prev, curr = curr, curr.next
            left -= 1
            right -= 1

        # reverse
        beforeRev, firstRev = prev, curr
        while right > 0:
            curr.next, curr, prev = prev, curr.next, curr
            right -= 1

        # stitch back together
        if beforeRev is not None: beforeRev.next = prev
        else: head = prev
        firstRev.next = curr

        
        return head


testcases = [
    ([1,2,3,4,5], 2, 4, [1,4,3,2,5]),
    ([5], 1, 1, [5]),
    ([3,5], 1, 1, [3,5])
]

for i, (input, left, right, target) in enumerate(testcases):
    head = ListNode(input[0])
    node = head
    for entry in input[1:]:
        next = ListNode(entry)
        node.next = next
        node = next
    output = []
    reversedList = Solution().reverseBetween2Pass(head, left, right)
    while reversedList is not None:
        output.append(reversedList.val)
        reversedList = reversedList.next
    print('Case #{}: should be\n{}, is\n{}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')

