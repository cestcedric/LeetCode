class Solution:
    # O(n^2) time complexity: inner loop growing from 1 to numRows iterations
    # O(k) space complexity: no additional calls or memory besides the output list
    def generate(self, numRows: int) -> list:
        if numRows == 1: return [[1]]
        rows = [[1], [1,1]]
        for r in range(3, numRows+1):
            row = [1]
            for i in range(1, r-1):
                row.append(rows[-1][i-1] + rows[-1][i])
            row.append(1)
            rows.append(row)
        return rows


testcases = [
    (5, [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]),
    (1, [[1]])
]

for i, (input, target) in enumerate(testcases):
    output = Solution().generate(input)
    print('Case #{}: should be:\n{}, is\n{}'.format(i+1, target, output))
    assert target == output
print('All test cases passed!')
        