class Solution:
    def matrixRankTransform(self, matrix: list) -> list:
        #TODO:
        pass


testcases = [
    ([[1,2],[3,4]], [[1,2],[2,3]]),
    ([[7,7],[7,7]], [[1,1],[1,1]]),
    ([[20,-21,14],[-19,4,19],[22,-47,24],[-19,4,19]], [[4,2,3],[1,3,4],[5,1,6],[1,3,4]]),
    ([[7,3,6],[1,4,5],[9,8,2]], [[5,1,4],[1,2,3],[6,3,1]])
]


for i, (matrix, target) in enumerate(testcases):
    output = Solution().matrixRankTransform(matrix)
    print('Case #{}: should be'.format(i + 1))
    for row in target:
        print(row)
    print('is')
    for row in output:
        print(row)
    assert target == output
print('All test cases passed!')