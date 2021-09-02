from functools import lru_cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

        
class Solution:
    # O(exponential) time, probably Catalan numbers
    # same for space
    def generateTrees(self, n: int) -> list:
        
        @lru_cache(None)
        def buildBST(a, b):
            if a == b: return [None]
            output = []    
            
            for i in range(a, b):
                # build trees for a <= x < i
                for smaller in buildBST(a, i):
                    # combine with every tree containing i <= x < b
                    for bigger in buildBST(i + 1, b):
                        root = TreeNode(i)
                        root.left = smaller
                        root.right = bigger
                        output.append(root)
                        
            return output
        
        return buildBST(1, n + 1)
            
        
            
        