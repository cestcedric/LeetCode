# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time complexity: look at each node once
    # O(h) space complexity: call stack depth
    def pathSum(self, root: TreeNode, targetSum: int) -> list:
        if root is None: return []

        def isLeaf(node):
            return node.left is None and node.right is None

        output = []

        def dfs(node: TreeNode, sequence, target):
            nonlocal output
            if node is None: return
            if isLeaf(node):
                if target == node.val: output.append(sequence + [node.val])
                return

            sequence.append(node.val)
            dfs(node.left, sequence[::], target - node.val)
            dfs(node.right, sequence[::], target - node.val)

        dfs(root, [], targetSum)
        return output
        

node1 = TreeNode(1)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(5)
node6 = TreeNode(6)
node7 = TreeNode(7)
node8 = TreeNode(8)
node1.left, node1.right = node2, node3
node2.left, node2. right = node4, node5
node3.left, node3.right = node6, node7
node7.right = node8

print(Solution().pathSum(node1, 7))