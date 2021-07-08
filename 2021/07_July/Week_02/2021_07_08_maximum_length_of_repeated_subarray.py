class Solution:
    # O(m * n) time complexity: every entry in dp computed once, then max op over all rows
    # O(m * n) space complexity: dp array with m * n entries
    def findLength(self, nums1: list, nums2: list) -> int:
        m, n = len(nums1), len(nums2)
        dp = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if (i == 0 or j == 0) and nums1[i] == nums2[j]: dp[i][j] = 1
                elif nums1[i] == nums2[j]: dp[i][j] = dp[i - 1][j - 1] + 1

        return max([max(row) for row in dp])


testcases = [
    ([1,2,3,2,1], [3,2,1,4,7], 3),
    ([0,0,0,0,0], [0,0,0,0,0], 5),
    ([0,0,0,0,0], [1,1], 0)
]
        
for i, (nums1, nums2, target) in enumerate(testcases):
    output = Solution().findLength(nums1, nums2)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')