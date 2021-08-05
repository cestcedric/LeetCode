from functools import lru_cache

class Solution:
    # O(1) time and space: analyze situation and build up from small examples
    def stoneGameEZ(self, piles: list) -> bool:
        return True


    # O(n^2) time and space: DP for all combinations of i and j
    # Points for opponent are counted as negative points for player
    def stoneGame(self, piles: list) -> bool:
        
        @lru_cache(None)
        def dp(i, j):
            nonlocal piles

            if i == j: 
                return -piles[i]

            if (i + j) % 2 == 0: 
                return max(dp(i + 1, j) - piles[i], dp(i, j - 1) - piles[j])
            else:
                return max(dp(i + 1, j) + piles[i], dp(i, j - 1), + piles[j])

        return dp(0, len(piles) - 1) > 0






testcases = [
    ([5,3,4,5], True),
    ([1,3,2,1], True),
    ([1,2], True)
]

for i, (piles, target) in enumerate(testcases):
    output = Solution().stoneGame(piles)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')