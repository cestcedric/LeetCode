class Solution:
    # O(n) time complexity: traverse nums once
    # O(1) space complexity: constant number of extra variables used
    def numSubarrayBoundedMax(self, nums: list, left: int, right: int) -> int:
        if nums == []: return 0
        total = 0

        # left end of array
        l = 0
        # already encountered correct max element?
        supported = False
        # take care of non-support elements: 
        # [2,1,1,1,3,4], left = 2, right = 3
        # => 2, 21, 211, 2111, 21113
        # => 1113, 113, 13, 3
        # but not 111, 11, 1
        unsupported = 0
        for r in range(len(nums)):
            # add single element array, all arrays up to r
            if nums[r] >= left and nums[r] <= right:
                total += 1 + r - l
                supported = True
                unsupported = 0
            # barrier, start from here
            elif nums[r] > right:
                l = r + 1
                supported = False
            # new non-support element
            elif nums[r] < left and supported:
                total += r - l - unsupported
                unsupported += 1
        
        return total


testcases = [
    ([2, 1, 4, 3], 2, 3, 3),
    ([], 1, 3, 0),
    ([1,2,3,4,5], 2, 4, 9),
    ([2,9,2,5,6], 2, 8, 7),
    ([7,3,6,7,1], 1, 4, 2),
    ([73,55,36,5,55,14,9,7,72,52], 32, 69, 22)
]

for i, (nums, left, right, target) in enumerate(testcases):
    output = Solution().numSubarrayBoundedMax(nums, left, right)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')