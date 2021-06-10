# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# O(n) time complexity: 'inorder_map' allows for O(1) lookup, n nodes => O(n)
# O(n) space complexity: 'inorder_map' obviously needs space
class Solution:
    def buildTree(self, preorder: list, inorder: list) -> TreeNode:
        def buildTreeRec(left, right):
            nonlocal pre_index
            if left > right: return None

            root = TreeNode(preorder[pre_index])
            pre_index += 1

            root.left = buildTreeRec(left, inorder_map[root.val] - 1)
            root.right = buildTreeRec(inorder_map[root.val] + 1, right)

            return root

        pre_index = 0
        inorder_map = {node: i for i, node in enumerate(inorder)}
        return buildTreeRec(0, len(preorder)-1)
        