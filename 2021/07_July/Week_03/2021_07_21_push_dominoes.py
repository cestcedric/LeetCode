class Solution:
    # O(n) time complexity: three passes through array
    # O(n) space complexity: extra space for dpLeft and dpRight, n elements each
    def pushDominoes(self, dominoes: str) -> str:
        dominoes = list(dominoes)
        n = len(dominoes)
        dpRight = [n if d == 'R' else 0 for d in dominoes]
        dpLeft = [-n if d == 'L' else 0 for d in dominoes]

        for i in range(1, len(dominoes)):
            if dominoes[i] != '.': continue
            if dpRight[i - 1] > 0: dpRight[i] += dpRight[i - 1] - 1

        for i in range(len(dominoes) - 2, -1, -1):
            if dominoes[i] != '.': continue
            if dpLeft[i + 1] < 0: dpLeft[i] += dpLeft[i + 1] + 1

        for i in range(len(dominoes)):
            if dpLeft[i] + dpRight[i] > 0: dominoes[i] = 'R'
            elif dpLeft[i] + dpRight[i] < 0: dominoes[i] = 'L'

        return ''.join(dominoes)


testcases = [
    ('RR.L', 'RR.L'),
    ('.L.R...LR..L..', 'LL.RR.LLRRLL..'),
    ('..R..', '..RRR')
]

for i, (dominoes, target) in enumerate(testcases):
    output = Solution().pushDominoes(dominoes)
    print('Case #{}: should be\n{}, is\n{}'.format(i + 1, target, output))
    assert target == output
print('All test cases passed!')