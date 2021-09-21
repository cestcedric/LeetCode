class Solution:
    # O(n) time: one pass through nums
    # O(1) space
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        start = 0
        maxLength = 0

        for end, x in enumerate(nums):
            if x == 1: maxLength = max(maxLength, end - start + 1)
            else: start = end + 1

        return maxLength


testcases = [
    ([1,1,0,1,1,1], 3),
    ([1,0,1,1,0,1], 2)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().findMaxConsecutiveOnes(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')