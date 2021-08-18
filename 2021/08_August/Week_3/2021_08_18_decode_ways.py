from functools import lru_cache

class Solution:
    # O(n) time: n = len(s) different stats, two transitions from each state at most
    # O(n) space: cache and call stack
    def numDecodings(self, s: str) -> int:
        
        @lru_cache(None)
        def dfs(s, index):
            if index == len(s): return 1
            if s[index] == '0': return 0

            total = 0
            # '1106' -> '106'
            total += dfs(s, index + 1)

            # '1106' -> '06'
            if index < len(s) - 1 and int(s[index:index + 2]) < 27:
                total += dfs(s, index + 2)

            return total

        return dfs(s, 0)


    # O(n) time: same as above
    # O(n) space: clearly we allocate an array of size n
    def numDecodingsDP(self, s: str) -> int:
        if s[0] == '0': return 0
        n = len(s)
        if n == 1: return 1

        dp = [0] * len(s)
        dp[n - 1] = 1 if s[-1] != '0' else 0

        end = int(s[-2:])
        if s[-2] != '0': dp[n - 2] += dp[n - 1]
        if 10 <= end < 27: dp[n - 2] += 1

        for i in range(n - 3, -1, -1):
            if s[i] == '0': continue
            
            dp[i] += dp[i + 1]
            if int(s[i:i + 2]) < 27: dp[i] += dp[i + 2]

        return dp[0]


testcases = [
    ('12', 2),
    ('226', 3),
    ('0', 0),
    ('06', 0),
    ('230', 0),
    ('10', 1),
    ('12120', 3)
]

for i, (s, target) in enumerate(testcases):
    output = Solution().numDecodingsDP(s)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')