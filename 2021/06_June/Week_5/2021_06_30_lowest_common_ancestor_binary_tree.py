from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # O(n) time complexity: DFS with O(n) potentially performed almost n times, but caching
    # O(n) space complexity: caching and callstack
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q: return root

        @lru_cache(None)
        def dfs(node, find):
            if node is None: return False
            if node == find: return True
            return dfs(node.left, find) or dfs(node.right, find)

        node = root
        while node is not None:
            if node == p or node == q: return node

            locationP = node.left if dfs(node.left, p) else node.right
            locationQ = node.left if dfs(node.left, q) else node.right
            
            if locationP != locationQ: return node
            node = locationP

    # O(n) time complexity: no caching needed, one pass through at most n nodes
    # O(log(n)) space complexity: call stack depth
    def lowestCommonAncestor2(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root == p or root == q: return root
        if root is None: return None

        left = self.lowestCommonAncestor2(root.left, p, q)
        right = self.lowestCommonAncestor2(root.right, p, q)

        if left and right: return root
        return left or right

