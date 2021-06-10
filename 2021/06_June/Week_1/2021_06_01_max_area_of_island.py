class Solution:
    def maxAreaOfIsland(self, grid: list) -> int:
        # O(n*m) time and space complexity
        # 'discovered' hashmap minimizes double exploration
        # Optimization possible by indicating from where we explore to eliminate final recursion step
        dims = (len(grid), len(grid[0]))
        discovered = {}
        maxArea = 0

        def explore(dims, grid, x, y):
            if x < 0 or y < 0 or x >= dims[0] or y >= dims[1]: return 0
            if 'x{}y{}'.format(x,y) in discovered: return 0
            discovered['x{}y{}'.format(x,y)] = grid[x][y]
            if grid[x][y] == 0: return 0
            left = explore(dims, grid, x, y+1)
            right = explore(dims, grid, x, y-1)
            up = explore(dims, grid, x-1, y)
            down = explore(dims, grid, x+1, y)
            return left + right + up + down + 1

        for x in range(dims[0]):
            for y in range(dims[1]):
                maxArea = max(maxArea, explore(dims, grid, x, y))

        return maxArea


testcases = [
    ([[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],[0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]], 6),
    ([[0,0,0,0,0,0,0,0]], 0)
]

for i, (input, target) in enumerate(testcases):
    output = Solution().maxAreaOfIsland(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')