# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # O(n) time complexity
    # O(log(n)) space complexity: call stack (assuming a balanced BST, else O(n))
    def lowestCommonAncestorRec(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if root.val in [p.val, q.val]: return root
        if root.val < p.val and root.val < q.val: 
            return self.lowestCommonAncestor(root.right, p, q)
        if root.val > p.val and root.val > q.val:
            return self.lowestCommonAncestor(root.left, p, q)
        return root


    # O(n) time complexity
    # O(1) space complexity: no extra space allocated for any variables
    def lowestCommonAncestorIt(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':  
        while root != None:
            if root.val in [p.val, q.val]: return root
            if root.val < p.val and root.val < q.val:
                root = root.right
                continue
            if root.val > p.val and root.val > q.val:
                root = root.left
                continue
            return root