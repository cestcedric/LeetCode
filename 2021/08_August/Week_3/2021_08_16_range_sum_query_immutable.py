from itertools import accumulate

class NumArray:

    # O(n) time and space
    def __init__(self, nums: list):
        self.cumSum = [0] + list(accumulate(nums))
        
    # O(1) time
    def sumRange(self, left: int, right: int) -> int:
        return self.cumSum[right + 1] - self.cumSum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
numArray = NumArray([-2, 0, 3, -5, 2, -1]);
print(numArray.sumRange(0, 2)); # return (-2) + 0 + 3 = 1
print(numArray.sumRange(2, 5)); # return 3 + (-5) + 2 + (-1) = -1
print(numArray.sumRange(0, 5)); # return (-2) + 0 + 3 + (-5) + 2 + (-1) = -3