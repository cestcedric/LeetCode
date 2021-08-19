# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time: visit each node once to compute subtree sum, once to compute product
    # O(n) space: dictionary containing the subtree sums
    def maxProduct(self, root: TreeNode) -> int:
        MOD = 10 ** 9 + 7
        # 1. get sum of all subtrees
        
        def dfs(node: TreeNode):
            nonlocal sums
            if node is None: return 0

            nodeSum = node.val
            nodeSum += dfs(node.left)
            nodeSum += dfs(node.right)

            sums[id(node)] = nodeSum

            return nodeSum

        sums = {}
        totalSum = dfs(root)

        # 2. find biggest product of (total sum - subsum) * subsum
        maxProduct = max(subSum * (totalSum - subSum) for subSum in sums.values())

        return maxProduct % MOD
