from collections import defaultdict

class Solution:
    # O(n^2) time
    # O(n^2) space
    def numberOfArithmeticSlices(self, nums: list) -> int:
        n = len(nums)
        if n < 3: return 0

        dp = [None] * n
        sliceCount = 0

        for i in range(n):
            dp[i] = defaultdict(int)
            for j in range(i):
                d = nums[i] - nums[j]
                dp[i][d] = dp[i][d] + dp[j][d] + 1
                sliceCount += dp[j][d]

        return sliceCount



testcases = [
    ([2,4,6,8,10], 7),
    ([7,7,7,7,7], 16)
]

for i, (nums, target) in enumerate(testcases):
    output = Solution().numberOfArithmeticSlices(nums)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        