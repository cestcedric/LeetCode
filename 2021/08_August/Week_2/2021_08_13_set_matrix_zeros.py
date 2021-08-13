class Solution:
    # O(m * n) time
    # O(1) space
    def zeroToNone(self, matrix: list) -> None:
        m, n = len(matrix), len(matrix[0])

        zeroInFirstRow = False
        zeroInFirstCol = False

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    if i == 0: zeroInFirstRow = True
                    if j == 0: zeroInFirstCol = True
                    matrix[i][0] = None
                    matrix[0][j] = None

        return zeroInFirstRow, zeroInFirstCol


    # O(m + n) time
    # O(1) space
    def noneToZero(self, matrix: list) -> None:
        m, n = len(matrix), len(matrix[0])

        for i in range(m):
            if matrix[i][0] == None: matrix[i][0] = 0

        for j in range(n):
            if matrix[0][j] == None: matrix[0][j] = 0


    # O(n) time
    # O(1) space
    def rowToZero(self, matrix: list, row) -> None:
        n = len(matrix[row])

        for j in range(1, n):
            if matrix[row][j] is not None: matrix[row][j] = 0


    # O(m) time
    # O(1) space
    def colToZero(self, matrix: list, col) -> None:
        m = len(matrix)

        for i in range(1, m):
            if matrix[i][col] is not None: matrix[i][col] = 0


    # O(n * m) time
    # O(1) space
    # store zero occurrences in first row / column
    # if matrix[0][0] is not zero we get issues with this None
    # => store that info separately
    def setZeroes(self, matrix: list) -> None:
        m, n = len(matrix), len(matrix[0])

        zeroInFirstRow, zeroInFirstCol = self.zeroToNone(matrix)
        if zeroInFirstRow != zeroInFirstCol: matrix[0][0] = 0

        for i in range(m):
            if matrix[i][0] == None:
                self.rowToZero(matrix, i)

        for j in range(n):
            if matrix[0][j] == None:
                self.colToZero(matrix, j)

        if zeroInFirstRow:
            self.rowToZero(matrix, 0)

        if zeroInFirstCol:
            self.colToZero(matrix, 0)

        self.noneToZero(matrix)
        


testcases = [
    ([[1,1,1],[1,0,1],[1,1,1]], [[1,0,1],[0,0,0],[1,0,1]]),
    ([[0,1,2,0],[3,4,5,2],[1,3,1,5]], [[0,0,0,0],[0,4,5,0],[0,3,1,0]]),
    ([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]], [[0,0,3,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]),
    ([[1,0,3]], [[0,0,0]])
]


for i, (matrix, target) in enumerate(testcases):
    Solution().setZeroes(matrix)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, matrix))
    assert target == matrix
print('All test cases passed!')