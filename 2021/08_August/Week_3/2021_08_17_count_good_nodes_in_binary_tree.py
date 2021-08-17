

# Definition for a binary tree node.
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time: look at each node once
    # => assuming popleft in O(1), could also use for node, maxVal in frontier
    # O(n) space: queue
    def goodNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        count = 0
        queue = deque([root, root.val])

        while queue:
            node, maxVal = queue.popleft()
            if maxVal <= node.val: 
                count += 1
            if node.left is not None: 
                queue.append((node.left, max(maxVal, node.val)))
            if node.right is not None:
                queue.append((node.right, max(maxVal, node.val)))

        return count

