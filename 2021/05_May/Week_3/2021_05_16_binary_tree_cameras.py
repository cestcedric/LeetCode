# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minCameraCover(self, root: TreeNode) -> int:
        # O(n) time, O(n) space since hashmap used
        # setting a camera up at an uncovered parent node is at least as good as at the child nodes
        self.cameras = 0
        covered = {None}

        def dfs(node, parent=None):
            if node:
                dfs(node.left, node)
                dfs(node.right, node)

                if (node not in covered and parent is None) or node.left not in covered or node.right not in covered:
                    self.cameras += 1
                    covered.update({node, parent, node.left, node.right})

        dfs(root)
        return self.cameras
