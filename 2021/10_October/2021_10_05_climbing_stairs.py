class Solution:
    # O(n) time
    # O(n) space
    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        
        dp = [0] * n
        dp[0], dp[1] = 1, 2
        
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
            
        return dp[n - 1]


testcases = [
    (2, 2),
    (3, 3),
    (25, 121393)
]

for i, (n, target) in enumerate(testcases):
    output = Solution().climbStairs(n)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')