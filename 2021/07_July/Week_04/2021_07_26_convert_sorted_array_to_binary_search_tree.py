# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # O(n) time complexity: visit each entry once
    # O(n) space complexity: copies of nums of size n/2, n/4, n/8, ... 
    def sortedArrayToBSTcopy(self, nums: list) -> TreeNode:
        if nums == []: return None
        mid = len(nums) // 2
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid + 1:])
        return node


    # O(n) time complexity: still have to look at each entry once
    # O(1) space complexity: no copying required
    # Faster than sortedArrayToBSTcopy, since no copying
    def sortedArrayToBST(self, nums: list) -> TreeNode:
        if nums == []: return None

        def dfs(start, end):
            nonlocal nums
            if start > end: return None
            mid = (start + end) // 2
            node = TreeNode(nums[mid])
            node.left = dfs(start, mid - 1)
            node.right = dfs(mid + 1, end)
            return node

        return dfs(0, len(nums))