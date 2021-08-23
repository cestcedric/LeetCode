# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time: have to look at each node once, then O(1) lookup in entries
    # O(n) space: additional set for quick lookup
    def findTarget(self, root: TreeNode, k: int) -> bool:
        stack = [root]
        entries = set()

        while stack != []:
            node = stack.pop()
            if k - node.val in entries: return True
            if node.left is not None: stack.append(node.left)
            if node.right is not None: stack.append(node.right)
            entries.add(node.val)

        return False

        


