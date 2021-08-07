from collections import defaultdict
from functools import lru_cache


class Solution:
    # O(n^2) time and space: 
    # O(n^2) to find possible palindromes, caching for quick traversal
    def minCut(self, s):
        d, n = defaultdict(set), len(s)
        
        # O(n)
        def helper(i, j):
            while i >= 0 and j < n and s[i] == s[j]:
                d[i].add(j)
                i, j = i - 1, j + 1
        
        # O(n^2)
        for k in range(n):
            helper(k, k)
            helper(k, k + 1)

        # O(n^2)
        @lru_cache(None)
        def dp(i):
            if i == -1: return 0
            return min([dp(k-1) + 1 for k in range(0, i+1) if i in d[k]])
        
        return dp(n-1) - 1

        




testcases = [
    ('aab', 1),
    ('a', 0),
    ('ab', 1),
    ('abc', 2),
    ('racecarbcb', 1)
]

for i, (s, target) in enumerate(testcases):
    output = Solution().minCut(s)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')