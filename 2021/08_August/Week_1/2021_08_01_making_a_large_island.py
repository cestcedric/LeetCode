class Solution:
    # O(1) time and space complexity
    @staticmethod
    def getNeighbours(grid, x, y):
        m, n = len(grid), len(grid[0])
        neighbours = []
        if x > 0: neighbours.append((x - 1, y))
        if x < m - 1: neighbours.append((x + 1, y))
        if y > 0: neighbours.append((x, y - 1))
        if y < n - 1: neighbours.append((x, y + 1))
        return neighbours
    
    @staticmethod
    # O(m*m) time and space complexity: visited set of size <= m*n to only visit once
    def areaDFS(grid, x, y, areaID):
        visited = set()

        def dfs(x, y, index):
            nonlocal grid, visited
            if (x, y) in visited: return 0
            visited.add((x, y))
            if grid[x][y] == 0: return 0
            total = 1
            grid[x][y] = index
            for r, c in Solution().getNeighbours(grid, x, y):
                if (r, c) in visited: continue
                total += dfs(r, c, index)
            return total

        return dfs(x, y, areaID)


    @staticmethod
    # O(1) time and space complexity: max. 4 neighbours for each field
    def connectAreas(grid, x, y):
        neighbours = Solution().getNeighbours(grid, x, y)
        areas = set(grid[r][c] for r, c in neighbours)
        return areas

    # O(m*n) time complexity: visit each node once
    # O(n*m) space complexity: call stack depth, visited sets and areas dict
    def largestIsland(self, grid: list) -> int:
        m, n = len(grid), len(grid[0])
        # find all zero entries, sizes for areas
        zeros = []
        areas, areaID, maxArea = {}, 2, 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0: zeros.append((i, j))
                elif grid[i][j] == 1: 
                    areas[areaID] = self.areaDFS(grid, i, j, areaID)
                    maxArea = max(maxArea, areas[areaID])
                    areaID += 1

        # check area combinations by setting 0 -> 1
        for x, y in zeros:
            connectedArea = 0
            for areaID in self.connectAreas(grid, x, y):
                if areaID != 0: connectedArea += areas[areaID]
            maxArea = max(maxArea, connectedArea + 1)

        return maxArea


testcases = [
    ([[1,0],[0,1]], 3),
    ([[1,1],[1,0]], 4),
    ([[1,1],[1,1]], 4),
    ([[1,1,1],[0,0,1],[1,1,0]], 7)
]

for i, (grid, target) in enumerate(testcases):
    output = Solution().largestIsland(grid)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed')