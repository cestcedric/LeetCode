# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Memory-efficient: list is directly transformed to tree, O(n) space
    # Finding middle of list is no efficient, so O(n log(n)) runtime
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        p_slow, p_fast, p_prev = head, head, None

        # find middle with p_slow, p_prev end of left part, p_fast end of tree
        while p_fast.next:
            p_prev = p_slow
            p_slow = p_slow.next
            p_fast = p_fast.next
            if p_fast.next:
                p_fast = p_fast.next
        
        if p_prev == None:
            return TreeNode(p_slow.val)

        # split tree
        # left part: start -> p_prev
        # right part: p_slow.next -> end
        p_prev.next = None
        root = TreeNode(p_slow.val)
        root.left = self.sortedListToBST(head)
        root.right = self.sortedListToBST(p_slow.next)
        return root

        

def printTree(tree):
    if not tree:
        return 'None'
    return '{} {} {}'.format(tree.val, printTree(tree.left), printTree(tree.right))


items = [-10, -3, 0, 1, 5, 9]
head = ListNode(items[0])
t = head
for i in items[1:]:
    t.next = ListNode(i)
    t = t.next


tree = Solution().sortedListToBST(head)
print(printTree(tree))

        