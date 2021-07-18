# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # O(n) time complexity: 
    # -> loop over each node once
    # -> n // k times: reverse list in O(k)
    #  => O(n // k * k) = O(n) total reversing time complexity
    # O(n) space complexity: only dependent on reverseList implementation
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head.next is None: return head
        # if k == 1: return head # shortcut
        sentinel = ListNode()
        sentinel.next = head
        pred, first, node, i = sentinel, head, head, 1

        while node is not None:
            if i < k:
                node = node.next
                i += 1
            else:
                succ = node.next
                node.next = None
                pred.next, pred = self.reverseList(first)
                first = pred.next = node = succ
                i = 1

        return sentinel.next

    # O(n) time complexity: looks at every node twice
    # O(1) space complexity
    def reverseList(self, node):
        if node is None: return None, None
        
        last = node
        prev, succ = None, node.next
        while succ is not None:
            node.next = prev
            prev = node
            node = succ
            succ = succ.next
        node.next = prev

        return node, last


def linkedListToArray(node):
    output = []
    while node is not None:
        output.append(node.val)
        node = node.next
    return output

def arrayToLinkedList(arr):
    head = ListNode(arr[0])
    node = head
    for n in arr[1:]:
        node.next = ListNode(n)
        node = node.next
    return head

testcases = [
    ([1, 2, 3, 4, 5], 3, [3, 2, 1, 4, 5]),
    ([1, 2, 3, 4, 5], 1, [1, 2, 3, 4, 5]),
    ([1], 1, [1])
]

for i, (nodes, k, target) in enumerate(testcases):
    head = arrayToLinkedList(nodes)
    output = Solution().reverseKGroup(head, k)
    outputArr = linkedListToArray(output)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, outputArr))
    assert target == outputArr
print('All test cases passed!')