class Solution:
    # O(n*k) time complexity
    # O(n*k) space complexity
    def kInversePairs(self, n: int, k: int) -> int:
        if n == 0: return 0
        if k == 0: return 1
        dp = [[1] + [0 for _ in range(k)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, k+1):
                dp[i][j] = dp[i][j-1] + dp[i-1][j] - (i <= j) * dp[i - 1][max(j - i, 0)]       
        return dp[n][k] % (10**9 + 7)

        


testcases = [
    (6, 7, 90),
    (3, 0, 1),
    (3, 1, 2),
    (3, 2, 2)
]

for i, (n, k, target) in enumerate(testcases):
    output = Solution().kInversej(n, k)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')