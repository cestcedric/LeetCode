class Solution:
    # O(m * n) time: m rows, n cols
    # Not even worst case upper bound, we literally check all m * n entries
    # O(1) space
    def islandPerimeter(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        perimeter = 0

        def getBorder(r, c):
            nonlocal grid, m, n
            borders = 4

            if 0 < r and grid[r - 1][c] == 1: borders -= 1
            if r < m -1 and grid[r + 1][c] == 1: borders -= 1
            if 0 < c and grid[r][c - 1] == 1: borders -= 1
            if c < n - 1 and grid[r][c + 1] == 1: borders -= 1

            return borders

        for r in range(m):
            for c in range(n):
                if grid[r][c] == 0: continue
                perimeter += getBorder(r, c)

        return perimeter


testcases = [
    ([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]], 16),
    ([[1]], 4),
    ([[1,0]], 4)
]

for i, (grid, target) in enumerate(testcases):
    output = Solution().islandPerimeter(grid)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        