class Solution:
    # O(n) time complexity: one pass through s
    # O(n) space complexity: dp array with n + 1 entries
    # Can reduce space complexity by only storing dp[i - 1] and dp[i]
    def numDecodings(self, s: str) -> int:
        n = len(s)
        MOD = 10 ** 9 + 7
        dp = [0] * (n + 1)

        dp[0] = 1
        if s[0] == '0': return 0
        if s[0] == '*': dp[1] = 9
        else: dp[1] = 1 

        for i in range(1, n):
            if s[i] == '*':
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == '1': dp[i + 1] += 9 * dp[i - 1]
                elif s[i - 1] == '2': dp[i + 1] += 6 * dp[i - 1]
                elif s[i - 1] == '*': dp[i + 1] += 15 * dp[i - 1]
            else:
                if s[i] == '0': dp[i + 1] = 0
                else: dp[i + 1] = dp[i]
                if s[i - 1] == '1': dp[i + 1] += dp[i - 1]
                elif s[i - 1] == '2' and int(s[i]) < 7: 
                    dp[i + 1] += dp[i - 1]
                elif s[i - 1] == '*':
                    if int(s[i]) < 7: dp[i + 1] += 2 * dp[i - 1]
                    else: dp[i + 1] += dp[i - 1]
            dp[i + 1] %= MOD
        return dp[n]


testcases = [
    ('*', 9),
    ('1*', 18),
    ('2*', 15),
    ('123**34*', 3078),
    ('11106', 2)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().numDecodings(input)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')