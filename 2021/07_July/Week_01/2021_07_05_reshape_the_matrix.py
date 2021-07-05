class Solution:
    # O(n) time complexity: match index from old and new array and copy in one pass
    # O(1) space complexity: no additional space used, other than the output list (O(n))
    def matrixReshape(self, mat: list, r: int, c: int) -> list:
        m, n = len(mat), len(mat[0])
        if m * n != r * c or (m, n) == (r, c): return mat

        row, column = 0, 0
        output = [[None] * c for _ in range(r)]
        for x in range(r):
            for y in range(c):
                output[x][y] = mat[row][column]
                column += 1
                if column == n:
                    column = 0
                    row += 1

        return output


testcases = [
    ([[1,2],[3,4]], 1, 4, [[1,2,3,4]]),
    ([[1,2],[3,4]], 2, 4, [[1,2],[3,4]])
]


for i, (mat, r, c, target) in enumerate(testcases):
    output = Solution().matrixReshape(mat, r, c)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')

        