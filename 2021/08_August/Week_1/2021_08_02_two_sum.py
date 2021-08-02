class Solution:
    # O(n) time complexity: one pass through nums, O(1) dict lookup
    # O(n) space complexity: numToIndex contains at most n elements
    def twoSum(self, nums: list, target: int) -> list:
        numToIndex = {}
        for i, n in enumerate(nums):
            if target - n in numToIndex: return [numToIndex[target - n], i]
            numToIndex[n] = i            


testcases = [
    ([2,7,11,15], 9, [0,1]),
    ([3,2,4], 6, [1,2]),
    ([3,3], 6, [0,1])
]

for i, (nums, target, expectedOutput) in enumerate(testcases):
    output = Solution().twoSum(nums, target)
    print('Case #{}: should be {}, is {}'.format(i + 1, expectedOutput, output))
    assert expectedOutput == output
print('All test cases passed!')