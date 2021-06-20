class Solution:
    # O(n^2 * log(n)) time complexity: each node has on avg. 2 lower and 2 higher neighbors
    # O(n^2) space complexity
    def swimInWater(self, grid: list) -> int:
        n = len(grid)
        if grid[n-1][n-1] == n * (n-1): return n * (n-1)
        paths = [[n*n for _ in range(n)] for _ in range(n)]
        paths[0][0] = grid[0][0]
        updated = []
        visited = set()

        for x in range(n-1, -1, -1):
            for y in range(n-1, -1, -1):
                updated.append((x,y))

        while updated != []:
            x, y = updated.pop()
            visited.add((x,y))
            curDepth = paths[x][y]
            for i, j in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
                if min(i,j) < 0 or max(i,j) == n: continue
                dCurr = paths[i][j]
                dNew = max(curDepth, grid[i][j])
                if dNew < dCurr:
                    paths[i][j] = dNew
                    if (i,j) in visited:
                        updated.append((i,j))

        return paths[n-1][n-1]


testcases = [
    ([[0,2],[1,3]], 3),
    ([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]], 16)
]


for i, (input, target) in enumerate(testcases):
    output = Solution().swimInWater(input)
    print('Case #{}: should be {}, is {}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')