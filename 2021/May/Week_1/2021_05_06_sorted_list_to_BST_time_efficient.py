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
    # Faster execution time, but uses more memory
    # Additional python list created to use index and slicing
    # O(n) time complexity
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        tmp = []
        while head:
            tmp.append(head)
            head = head.next

        def req(nodelist):
            l = len(nodelist)
            if l == 0:
                return None
            if l == 1:
                return TreeNode(nodelist[0].val)
            root = TreeNode(nodelist[l//2].val)
            root.left = req(nodelist[:l//2])
            root.right = req(nodelist[l//2+1:])
            return root

        return req(tmp)


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

        