# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> list:
        # Time complexity O(n)
        # Space complexity O(n)
        if root is None: return []
        levels = [[root]]
        l = 0
        added = True
        while added:
            added = False
            level = []
            for node in levels[-1]:
                if node.left is not None: 
                    level.append(node.left)
                    added = True
                if node.right is not None: 
                    level.append(node.right)
                    added = True
            if added: levels.append(level)
            l += 1

        for level in range(l):
            for i in range(len(levels[level])):
                node = levels[level][i]
                levels[level][i] = node.val if node is not None else None

        return levels



node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)

node1.left = node2
node1.right = node3
node2.left = node4
node2.right = node5
node3.left = node6
node4.left = node7
node5.right = node8

print(Solution().levelOrder(node1))