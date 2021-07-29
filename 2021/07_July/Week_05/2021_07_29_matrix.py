from collections import deque

class Solution:
    # O(1) time complexity
    # O(1) space complexity
    def getNeighbours(self, mat, x, y) -> list:
        m, n = len(mat), len(mat[0])
        neighbours = []

        if x > 0: neighbours.append((x - 1, y))
        if x < m - 1: neighbours.append((x + 1, y))
        if y > 0: neighbours.append((x, y - 1))
        if y < n - 1: neighbours.append((x, y + 1))

        return neighbours


    # O(m * n) time complexity: visit most nodes only once
    # O(m * n) space complexity: output same size as mat, but new array
    def updateMatrix(self, mat: list) -> list:
        m, n = len(mat), len(mat[0])
        output = [[10**5] * n for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0: 
                    output[i][j] = 0
                    queue.append((i, j))

        while queue:
            x, y = queue.popleft()
            for new_x, new_y in self.getNeighbours(mat, x, y):
                if output[new_x][new_y] > output[x][y] + 1:
                    output[new_x][new_y] = output[x][y] + 1
                    queue.append((new_x, new_y))

        return output


testcases = [
    ([[0,0,0],[0,1,0],[0,0,0]], [[0,0,0],[0,1,0],[0,0,0]]),
    ([[0,0,0],[0,1,0],[1,1,1]], [[0,0,0],[0,1,0],[1,2,1]]),
    ([[0],[0],[0],[0],[0]], [[0],[0],[0],[0],[0]])
]

for i, (mat, target) in enumerate(testcases):
    output = Solution().updateMatrix(mat)
    print('Case #{} should be:'.format(i + 1))
    for row in target:
        print(row)
    print('Output:')
    for row in output:
        print(row)

    assert target == output
print('All test cases passed!')