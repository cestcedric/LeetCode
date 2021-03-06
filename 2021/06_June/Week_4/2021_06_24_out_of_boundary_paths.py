from functools import lru_cache

class Solution:
    # O(m*n*maxMove) time complexity: compute every cell in constant time
    # O(m*n*maxMove) space complexity: obviously, we have the dp structure
    def findPaths(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        if maxMove == 0: return 1 if startRow in [-1, m] or startColumn in [-1, n] else 0
        
        dp = [[[0 for _ in range(n)] for _ in range(m)] for _ in range(maxMove + 1)]

        for i in range(maxMove + 1):
            if i == 0: continue
            for x in range(m):
                for y in range(n):
                    dp[i][x][y] += dp[i-1][x-1][y] if x > 0 else 1
                    dp[i][x][y] += dp[i-1][x+1][y] if x < m - 1 else 1
                    dp[i][x][y] += dp[i-1][x][y-1] if y > 0 else 1
                    dp[i][x][y] += dp[i-1][x][y+1] if y < n - 1 else 1

        MOD = 10**9 + 7

        return dp[maxMove][startRow][startColumn] % MOD


    # O(m*n*maxMove) time complexity: same computations as above
    # O(m*n*maxMove) space complexity: using cache instead of explicit structure
    def findPathsCache(self, m: int, n: int, maxMove: int, startRow: int, startColumn: int) -> int:
        MOD = 10**9 + 7

        @lru_cache(None)
        def dfs(x, y, z):
            nonlocal m, n
            if x in [-1, m] or y in [-1, n]: return 1
            if z == 0: return 0
            total = 0
            total += dfs(x - 1, y, z - 1)
            total += dfs(x + 1, y, z - 1)
            total += dfs(x, y - 1, z - 1)
            total += dfs(x, y + 1, z - 1)
            return total

        return dfs(startRow, startColumn, maxMove) % MOD


testcases = [
    (2, 2, 2, 0, 0, 6),
    (1, 3, 3, 0, 1, 12),
    (10, 10, 0, 5, 5, 0)
]

for i, (m, n, maxMove, startRow, startColumn, target) in enumerate(testcases):
    output = Solution().findPathsCache(m, n, maxMove, startRow, startColumn)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')