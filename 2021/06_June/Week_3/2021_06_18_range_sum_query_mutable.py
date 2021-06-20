import numpy as np

# Compute cumulative sum when updating array
# Works when not doing everything by hand, but using built-in functions
class NumArray:

    # O(n) time complexity if done with pure Python, numpy speeds cumulative sum up a lot
    # O(n) space complexity
    def __init__(self, nums: list):
        self.nums = nums
        self.cSum = np.cumsum(self.nums)

        
    # O(n) time complexity if done with pure Python, numpy again quicker
    # O(1) space complexity
    def update(self, index: int, val: int) -> None:
        diff = val - self.nums[index]
        self.nums[index] = val
        self.cSum[index:] += diff
        

    # O(1) time complexity
    # O(1) space complexity
    def sumRange(self, left: int, right: int) -> int:
        return self.cSum[right] - (self.cSum[left-1] if left > 0 else 0)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)