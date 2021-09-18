class Solution:
    def spiralOrder(self, matrix: list) -> list:
        m, n = len(matrix), len(matrix[0])
        if m == 1 or n == 1: return matrix

        top, bottom = 1, m - 1
        left, right = 1, n - 1

        x, y = 0, 0
        output = []

        while top <= bottom or left <= right:
            output.append(matrix[x][y])
            
            # TODO:


testcases = [
    ([[1,2,3],[4,5,6],[7,8,9]], [1,2,3,6,9,8,7,4,5]),
    ([[1,2,3,4],[5,6,7,8],[9,10,11,12]], [1,2,3,4,8,12,11,10,9,5,6,7])
]

for i, (matrix, target) in enumerate(testcases):
    output = Solution().spiralOrder(matrix)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')