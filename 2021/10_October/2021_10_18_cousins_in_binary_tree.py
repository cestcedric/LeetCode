# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time: worst case traverse whole tree
    # O(n) space: frontier contains at most n/2 elements
    def isCousinsIterative(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val == x or root.val == y: return False

        frontier = [root]
        levelX = False
        levelY = False

        while frontier != []:
            nextRow = []
            if levelX != levelY: return False

            for node in frontier:
                if node.left and node.right:
                    if node.left.val in (x, y) and node.right.val in (x, y):
                        return False
                if node.val == x: levelX = True
                if node.val == y: levelY = True
                if node.left: nextRow.append(node.left)
                if node.right: nextRow.append(node.right)
            
            frontier = nextRow
                
        return levelX == levelY


    # O(n) time: worst case still traverse whole tree
    # O(n) space: call stack for very unbalanced binary tree
    def isCousins(self, root: TreeNode, x: int, y: int) -> bool:
        if root.val in (x, y): return False

        parentX, levelX = None, None
        parentY, levelY = None, None

        def dfs(node: TreeNode, level: int) -> None:
            nonlocal x, y, parentX, parentY, levelX, levelY
            if node.left:
                if node.left.val == x: parentX, levelX = node.val, level
                if node.left.val == y: parentY, levelY = node.val, level

            if node.right:
                if node.right.val == x: parentX, levelX = node.val, level
                if node.right.val == y: parentY, levelY = node.val, level

            if parentX and parentY: return

            if node.left: dfs(node.left, level + 1)
            if node.right: dfs(node.right, level + 1)

        dfs(root, 1)

        return parentX != parentY and levelX == levelY

