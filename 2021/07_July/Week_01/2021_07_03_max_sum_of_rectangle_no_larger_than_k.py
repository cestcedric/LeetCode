from itertools import accumulate, combinations, product
from sortedcontainers import SortedList

# O(m^2 * n * log(n)) time complexity: O(n * log(n)) for rangeSumOfRow, 
# called m*m times
# O(n * m) space complexity: extra space for rows with cumulative sums
class Solution:
    def maxSumSubmatrix(self, matrix: list, k: int) -> int:
        def rangeSumOfRow(nums, k):
            sList, res = SortedList([0]), float('-inf')
            for n in accumulate(nums):
                i = sList.bisect_left(n - k)
                if i < len(sList): res = max(res, n - sList[i])
                sList.add(n)
            return res

        m, n, res = len(matrix), len(matrix[0]), float('-inf')

        for i, j in product(range(1, m), range(n)):
            matrix[i][j] += matrix[i - 1][j]

        matrix = [[0] * n] + matrix

        for x, y in combinations(range(m + 1), 2):
            row = [j - i for i, j in zip(matrix[x], matrix[y])]
            res = max(res, rangeSumOfRow(row, k))

        return res


testcases = [
    ([[1,0,1],[0,-2,3]], 2, 2),
    ([[2,2,-1]], 3, 3)
]

for i, (input, k, target) in enumerate(testcases):
    output = Solution().maxSumSubmatrix(input, k)
    print('Case #{}: should be {}, is {}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')
        