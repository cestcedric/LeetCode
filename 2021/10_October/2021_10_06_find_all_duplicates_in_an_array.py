class Solution:
    # O(n) time: one pass through nums
    # O(1) space: only new space needed is for output
    def findDuplicates(self, nums: list) -> list:
        duplicates = []
        
        for n in nums:
            if nums[abs(n) - 1] < 0: duplicates.append(abs(n))
            else: nums[abs(n) - 1] *= -1
                
        return duplicates
        